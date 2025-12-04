import React, { useEffect, useRef, useState } from 'react';
import { X, ZoomIn, ZoomOut, Maximize } from 'lucide-react';

const TreeModal = ({ isOpen, onClose, data }) => {
    if (!isOpen || !data) return null;

    const [scale, setScale] = useState(1);
    const [position, setPosition] = useState({ x: 0, y: 0 });
    const [isDragging, setIsDragging] = useState(false);
    const [dragStart, setDragStart] = useState({ x: 0, y: 0 });
    const svgRef = useRef(null);

    // Reset view when data changes
    useEffect(() => {
        setScale(1);
        setPosition({ x: 0, y: 0 });
    }, [data]);

    const handleWheel = (e) => {
        e.preventDefault();
        const scaleAdjustment = -e.deltaY * 0.001;
        const newScale = Math.max(0.1, Math.min(5, scale + scaleAdjustment));
        setScale(newScale);
    };

    const handleMouseDown = (e) => {
        setIsDragging(true);
        setDragStart({ x: e.clientX - position.x, y: e.clientY - position.y });
    };

    const handleMouseMove = (e) => {
        if (isDragging) {
            setPosition({
                x: e.clientX - dragStart.x,
                y: e.clientY - dragStart.y
            });
        }
    };

    const handleMouseUp = () => {
        setIsDragging(false);
    };

    // --- VISUALIZATION LOGIC ---
    const renderTree = () => {
        const mtData = data.master_theorem_data || {};
        const type = mtData.type;
        const elements = [];
        const maxDepth = 4; // Matching Python max_depth
        const levelCosts = {}; // Track costs per level to avoid duplicates

        // Helper to add SVG elements
        const addNode = (x, y, label, color, key, isLeaf = false) => {
            elements.push(
                <g key={`node-${key}`}>
                    {/* Glow effect */}
                    <circle cx={x} cy={y} r="25" fill={color} fillOpacity="0.3" />
                    {/* Core node */}
                    <circle cx={x} cy={y} r="18" fill={color} />
                    <text x={x} y={y} dy="5" textAnchor="middle" fill="white" fontSize="10" fontWeight="bold" style={{ pointerEvents: 'none' }}>{label}</text>
                </g>
            );
        };

        const addEdge = (x1, y1, x2, y2, label, key) => {
            elements.push(
                <g key={`edge-${key}`}>
                    <line x1={x1} y1={y1} x2={x2} y2={y2} stroke="#444" strokeWidth="1.5" strokeOpacity="0.6" />
                    {label && (
                        <g transform={`translate(${(x1 + x2) / 2}, ${(y1 + y2) / 2})`}>
                            <rect x="-12" y="-8" width="24" height="16" fill="#1e1e1e" fillOpacity="0.9" rx="4" />
                            <text x="0" y="4" textAnchor="middle" fill="#888" fontSize="9">{label}</text>
                        </g>
                    )}
                </g>
            );
        };

        const addCostAnalysis = (level, y, costText, detailText, color) => {
            if (levelCosts[level]) return;
            levelCosts[level] = true;

            const textX = 1000; // Moved extremely far right

            elements.push(
                <g key={`cost-${level}`}>
                    <text x={textX} y={y} fill={color} fontSize="14" fontWeight="bold" textAnchor="start">
                        {costText}
                    </text>
                    <text x={textX} y={y + 20} fill="#CCCCCC" fontSize="12" textAnchor="start">
                        {detailText}
                    </text>
                    {/* Dotted line connecting tree to cost */}
                    <line x1="500" y1={y} x2={textX - 20} y2={y} stroke="#333" strokeDasharray="4" />
                </g>
            );
        };

        const colors = ['#33C1FF', '#33FF57', '#FF33A8', '#FFC300', '#DAF7A6', '#FF5733'];

        // Recursive render functions
        const renderRecursive = (x, y, level, branchingFactor, label, mode, param) => {
            // Cost Analysis Logic (Ported from Python)
            const color = colors[Math.min(level, colors.length - 1)];

            if (mode === "sub") {
                const nodeCount = Math.pow(branchingFactor, level);
                const costLabel = "c"; // Simplified
                const costText = `Nivel ${level}`;
                const detailText = `${nodeCount} nodos × ${costLabel} = ${nodeCount}${costLabel}`;
                addCostAnalysis(level, y, costText, detailText, color);
            } else if (mode === "div") {
                const nodeCount = Math.pow(branchingFactor, level);
                let sizeStr = level === 0 ? "n" : `n/${Math.pow(parseInt(param), level)}`;

                // Assuming f(n) = c (constant) or cn (linear) based on label
                // Simplified logic for visualizer
                const nodeCostStr = label.includes("n") ? `c(${sizeStr})` : "c";
                const totalCostStr = label.includes("n") && branchingFactor == param ? "cn" : `${nodeCount}${nodeCostStr}`;

                const costText = `Nivel ${level}`;
                const detailText = `${nodeCount} nodos × ${nodeCostStr}`;
                addCostAnalysis(level, y, costText, detailText, color);
            }

            if (level > maxDepth) return;

            const key = `${x}-${y}-${level}`;

            // Draw Node
            let nodeLabel = label;
            if (mode === 'div') {
                nodeLabel = level === 0 ? "n" : `n/${Math.pow(parseInt(param), level)}`;
            }
            addNode(x, y, nodeLabel, color, key);

            // Draw Children
            if (level < maxDepth) {
                const width = 600 / Math.pow(branchingFactor, level * 0.8);
                const childY = y + 100; // Increased vertical spacing

                for (let i = 0; i < branchingFactor; i++) {
                    let offset = 0;
                    if (branchingFactor > 1) {
                        offset = (i - (branchingFactor - 1) / 2) * width;
                    }
                    const childX = x + offset;

                    addEdge(x, y + 20, childX, childY - 20, "", `${key}-${i}`);
                    renderRecursive(childX, childY, level + 1, branchingFactor, "", mode, param);
                }
            }
        };

        const renderCharacteristic = (x, y, level, lags, label) => {
            // Cost Analysis Logic
            const color = level === maxDepth ? '#E04F5F' : colors[Math.min(level, colors.length - 1)];

            const numChildren = lags.length;
            const nodeCountStr = `~${numChildren}^${level}`;
            const costText = `Nivel ${level}`;
            const detailText = `${nodeCountStr} nodos`;
            addCostAnalysis(level, y, costText, detailText, color);

            if (level > maxDepth) return;

            const key = `${x}-${y}-${level}`;
            const isLeaf = level === maxDepth;

            // Draw Node
            addNode(x, y, label, color, key, isLeaf);

            // Draw Children
            if (level < maxDepth) {
                // Adjusted spacing logic from Python: width = 600 / Math.pow(1.2, level) -> scaled for SVG (approx x60)
                const width = 600 / Math.pow(1.2, level);
                const childY = y + 100;

                lags.forEach((lag, i) => {
                    let offset = 0;
                    if (numChildren > 1) {
                        offset = (i - (numChildren - 1) / 2) * width;
                    }
                    const childX = x + offset;

                    // Calculate new label
                    let newLabel = "...";
                    if (label === "n") newLabel = `n-${lag}`;
                    else if (label.startsWith("n-")) {
                        try {
                            const curr = parseInt(label.split("-")[1]);
                            newLabel = `n-${curr + lag}`;
                        } catch (e) { }
                    }

                    // Edge label logic: n-1, n-2
                    const edgeLabel = `n-${lag}`;

                    addEdge(x, y + 20, childX, childY - 20, edgeLabel, `${key}-${i}`);
                    renderCharacteristic(childX, childY, level + 1, lags, newLabel);
                });
            }
        };

        // Main Draw Logic
        // Add separator line for Cost Analysis
        elements.push(
            <line key="separator" x1="950" y1="-50" x2="950" y2="500" stroke="#333" strokeWidth="2" strokeDasharray="5" />
        );
        elements.push(
            <text key="cost-header" x="1000" y="-20" fill="#888" fontSize="16" fontWeight="bold">ANÁLISIS DE COSTOS</text>
        );

        if (type === 'master_theorem') {
            const a = parseInt(mtData.a || 1);
            const b = parseFloat(mtData.b || 1);
            renderRecursive(0, 50, 0, a, "n", "div", b);
        } else if (type === 'characteristic_equation') {
            const lags = mtData.lags || [1, 2];
            renderCharacteristic(0, 50, 0, lags, "n");
        } else if (type === 'linear_recurrence') {
            const a = parseInt(mtData.a || 1);
            renderRecursive(0, 50, 0, a, "n", "sub", 1);
        } else {
            return (
                <text x="0" y="50" textAnchor="middle" fill="#888" fontSize="20">
                    No se detectó estructura recursiva estándar.
                </text>
            );
        }

        return elements;
    };

    return (
        <div className="modal-overlay" style={{
            position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
            backgroundColor: 'rgba(0, 0, 0, 0.85)', zIndex: 1000,
            display: 'flex', justifyContent: 'center', alignItems: 'center',
            backdropFilter: 'blur(5px)'
        }}>
            <div className="modal-content glass-panel" style={{
                width: '95%', height: '95%', position: 'relative',
                backgroundColor: '#1e1e1e', borderRadius: '12px', overflow: 'hidden',
                display: 'flex', flexDirection: 'column'
            }}>

                {/* Header */}
                <div style={{
                    padding: '1rem 1.5rem', borderBottom: '1px solid #333',
                    display: 'flex', justifyContent: 'space-between', alignItems: 'center',
                    background: 'rgba(255,255,255,0.05)'
                }}>
                    <div>
                        <h2 style={{ margin: 0, color: '#33C1FF', fontSize: '1.2rem' }}>Árbol de Recurrencia</h2>
                        <p style={{ margin: '4px 0 0 0', color: '#888', fontSize: '0.9rem' }}>
                            {data.recurrence_relation || "Análisis de estructura"}
                        </p>
                    </div>
                    <div style={{ display: 'flex', gap: '10px' }}>
                        <button className="btn-icon" onClick={() => setScale(s => s + 0.1)}><ZoomIn size={20} /></button>
                        <button className="btn-icon" onClick={() => setScale(s => Math.max(0.1, s - 0.1))}><ZoomOut size={20} /></button>
                        <button className="btn-icon" onClick={() => { setScale(1); setPosition({ x: 0, y: 0 }) }}><Maximize size={20} /></button>
                        <button className="btn-icon" onClick={onClose} style={{ marginLeft: '10px', color: '#ff5555' }}><X size={24} /></button>
                    </div>
                </div>

                {/* Canvas Area */}
                <div
                    style={{ flex: 1, overflow: 'hidden', cursor: isDragging ? 'grabbing' : 'grab', position: 'relative' }}
                    onMouseDown={handleMouseDown}
                    onMouseMove={handleMouseMove}
                    onMouseUp={handleMouseUp}
                    onMouseLeave={handleMouseUp}
                    onWheel={handleWheel}
                >
                    <svg
                        ref={svgRef}
                        width="100%"
                        height="100%"
                        viewBox="-800 -100 2400 900"
                        preserveAspectRatio="xMidYMin meet"
                    >
                        <g transform={`translate(${position.x}, ${position.y}) scale(${scale})`}>
                            {renderTree()}
                        </g>
                    </svg>

                    <div style={{ position: 'absolute', bottom: 20, left: 20, color: '#555', fontSize: '0.8rem', pointerEvents: 'none' }}>
                        Arrastra para mover • Rueda para zoom
                    </div>
                </div>

            </div>
        </div>
    );
};

export default TreeModal;
