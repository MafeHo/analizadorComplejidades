import React, { useState } from 'react';
import { Activity, List, BarChart2, AlertCircle, CheckCircle, FunctionSquare, Info, Table, Bot } from 'lucide-react';
import RecursionTree from './RecursionTree';

const ResultsPanel = ({ data, loading, error, activeView, setActiveView }) => {

    if (loading) {
        return (
            <div className="glass-panel" style={{ alignItems: 'center', justifyContent: 'center', height: '100%' }}>
                <div className="spinner"></div>
                <p style={{ marginTop: '1rem', color: 'var(--text-secondary)' }}>Analizando algoritmo...</p>
            </div>
        );
    }

    if (error) {
        return (
            <div className="glass-panel" style={{ borderColor: 'var(--accent-danger)' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--accent-danger)' }}>
                    <AlertCircle size={24} />
                    <h3 style={{ margin: 0 }}>Error en el análisis</h3>
                </div>
                <p style={{ marginTop: '10px', color: 'var(--text-secondary)' }}>{error}</p>
            </div>
        );
    }

    if (!data) {
        return (
            <div className="glass-panel" style={{ alignItems: 'center', justifyContent: 'center', height: '100%', color: 'var(--text-secondary)', textAlign: 'center' }}>
                <Activity size={48} style={{ marginBottom: '1rem', opacity: 0.5 }} />
                <p>Ejecuta un análisis para ver los resultados aquí.</p>
            </div>
        );
    }

    // Calculate final complexity for chart (Used for Cases view)
    let finalComp = "O(n)";
    const compValidated = data.complexity_validated || "";
    const compCalculated = data.complexity_calculated || "";

    const match = compValidated.match(/[OΘΩThetaOmega]+\s*\(([^)]+)\)/);
    if (match) {
        finalComp = match[0];
    } else if (compCalculated.includes("2^n") || compCalculated.includes("2**n")) {
        finalComp = "O(2^n)";
    } else if (compCalculated !== "Desconocida") {
        finalComp = compCalculated;
    }

    // Parse Trace Table
    const parseTraceTable = (markdownTable) => {
        if (!markdownTable || !markdownTable.includes('|')) return null;

        const lines = markdownTable.split('\n').filter(line => line.trim() !== '');
        // Filter out separator lines (e.g., |---|---|)
        const contentLines = lines.filter(line => !line.match(/^\|?\s*-+\s*\|/));

        if (contentLines.length < 2) return null;

        const headers = contentLines[0].split('|').map(h => h.trim()).filter(h => h !== '');
        const rows = contentLines.slice(1).map(line =>
            line.split('|').map(cell => cell.trim()).filter((cell, idx) => idx < headers.length || cell !== '')
        );

        return { headers, rows };
    };

    const traceData = parseTraceTable(data.trace_diagram);

    // Custom formatter for explanation text
    const formatExplanation = (text) => {
        if (!text) return "No hay explicación detallada disponible.";

        // Split by lines to handle headers properly
        const lines = text.split('\n');

        return lines.map((line, idx) => {
            // Handle Headers
            if (line.startsWith('#### ')) {
                return <h4 key={idx} style={{ color: 'var(--accent-primary)', marginTop: '1rem', marginBottom: '0.5rem' }}>{line.replace('#### ', '')}</h4>;
            }
            if (line.startsWith('### ')) {
                return <h3 key={idx} style={{ color: 'var(--text-primary)', marginTop: '1.5rem', marginBottom: '1rem', borderBottom: '1px solid var(--border-color)', paddingBottom: '0.5rem' }}>{line.replace('### ', '')}</h3>;
            }

            // Handle Bold and Code formatting inline
            const parts = line.split(/(\*\*.*?\*\*|`.*?`)/g);

            return (
                <p key={idx} style={{ marginBottom: '0.5rem', lineHeight: '1.6', color: 'var(--text-secondary)' }}>
                    {parts.map((part, pIdx) => {
                        if (part.startsWith('**') && part.endsWith('**')) {
                            return <strong key={pIdx} style={{ color: 'var(--text-primary)' }}>{part.slice(2, -2)}</strong>;
                        }
                        if (part.startsWith('`') && part.endsWith('`')) {
                            return <code key={pIdx} style={{ background: 'rgba(0,0,0,0.3)', padding: '2px 6px', borderRadius: '4px', fontFamily: 'monospace', color: 'var(--accent-secondary)' }}>{part.slice(1, -1)}</code>;
                        }
                        return part;
                    })}
                </p>
            );
        });
    };

    return (
        <div className="results-container" style={{ display: 'flex', flexDirection: 'column', gap: '1rem', height: '100%' }}>

            {/* Navigation Buttons Grid */}
            <div className="results-nav">
                <button
                    className={`nav-btn ${activeView === 'lines' ? 'active' : ''}`}
                    onClick={() => setActiveView('lines')}
                >
                    <List size={18} />
                    Línea a Línea
                </button>
                <button
                    className={`nav-btn ${activeView === 'cases' ? 'active' : ''}`}
                    onClick={() => setActiveView('cases')}
                >
                    <BarChart2 size={18} />
                    Casos
                </button>
                <button
                    className={`nav-btn ${activeView === 'recurrence' ? 'active' : ''}`}
                    onClick={() => setActiveView('recurrence')}
                >
                    <FunctionSquare size={18} />
                    Tipo de Algoritmo
                </button>
                <button
                    className={`nav-btn ${activeView === 'info' ? 'active' : ''}`}
                    onClick={() => setActiveView('info')}
                >
                    <Info size={18} />
                    Análisis
                </button>
                <button
                    className={`nav-btn ${activeView === 'trace' ? 'active' : ''}`}
                    onClick={() => setActiveView('trace')}
                >
                    <Table size={18} />
                    Prueba
                </button>
                <button
                    className={`nav-btn ${activeView === 'llm_comparison' ? 'active' : ''}`}
                    onClick={() => setActiveView('llm_comparison')}
                >
                    <Bot size={18} />
                    Verificación IA
                </button>
            </div>

            {/* Content Area */}
            <div className="glass-panel" style={{ flex: 1, overflowY: 'auto', position: 'relative' }}>

                {activeView === 'lines' && (
                    <div className="view-content fade-in">
                        <h3 className="section-title">Análisis Detallado</h3>
                        <div className="line-analysis-list">
                            {data.line_by_line && data.line_by_line.length > 0 ? (
                                data.line_by_line.map((log, idx) => (
                                    <div key={idx} className="line-item">
                                        <div className="line-number">Línea {log.line}</div>
                                        <div className="line-cost">{log.cost}</div>
                                    </div>
                                ))
                            ) : (
                                <div style={{ textAlign: 'center', padding: '2rem', color: 'var(--text-secondary)' }}>
                                    No hay detalles línea por línea disponibles.
                                </div>
                            )}
                        </div>
                    </div>
                )}

                {activeView === 'cases' && (
                    <div className="view-content fade-in">
                        <h3 className="section-title">Análisis de Casos</h3>

                        <div className="cases-grid">
                            <div className="case-card best-case">
                                <h4>Mejor Caso (Ω)</h4>
                                <div className="case-value">{data.case_best || "Ω(1)"}</div>
                                <p>Escenario más favorable de ejecución.</p>
                            </div>

                            <div className="case-card average-case">
                                <h4>Caso Promedio (Θ)</h4>
                                <div className="case-value">{data.case_average || finalComp.replace('O', 'Θ')}</div>
                                <p>Comportamiento esperado estadísticamente.</p>
                            </div>

                            <div className="case-card worst-case">
                                <h4>Peor Caso (O)</h4>
                                <div className="case-value">{data.case_worst || finalComp}</div>
                                <p>Escenario más costoso (cota superior).</p>
                            </div>
                        </div>
                    </div>
                )}

                {activeView === 'recurrence' && (
                    <div className="view-content fade-in">
                        <h3 className="section-title">Tipo de Algoritmo</h3>

                        <div style={{ marginBottom: '2rem' }}>

                            <div style={{
                                display: 'inline-block',
                                padding: '0.5rem 1rem',
                                background: data.recurrence_relation === "Algoritmo Iterativo" ? 'rgba(16, 185, 129, 0.2)' : 'rgba(59, 130, 246, 0.2)',
                                color: data.recurrence_relation === "Algoritmo Iterativo" ? '#34d399' : '#60a5fa',
                                borderRadius: '8px',
                                fontWeight: 'bold'
                            }}>
                                {data.recurrence_relation === "Algoritmo Iterativo" ? "ITERATIVO" : "RECURSIVO"}
                            </div>
                        </div>

                        {data.recurrence_relation !== "Algoritmo Iterativo" && (
                            <div style={{ marginBottom: '2rem' }}>
                                <h4 style={{ color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>Relación de Recurrencia</h4>
                                <div className="code-block" style={{ fontSize: '1.2rem', textAlign: 'center' }}>
                                    {data.recurrence_relation}
                                </div>

                                {/* Pasos de Resolución */}
                                {data.recurrence_steps && (
                                    <div style={{ marginTop: '1.5rem', textAlign: 'left' }}>
                                        <h4 style={{ color: 'var(--text-secondary)', marginBottom: '0.5rem', fontSize: '0.9rem' }}>Resolución Paso a Paso:</h4>
                                        <div style={{
                                            background: 'rgba(0,0,0,0.3)',
                                            padding: '1rem',
                                            borderRadius: '6px',
                                            fontFamily: 'monospace',
                                            whiteSpace: 'pre-wrap',
                                            color: '#e2e8f0',
                                            fontSize: '0.9rem',
                                            borderLeft: '3px solid var(--accent-primary)'
                                        }}>
                                            {data.recurrence_steps}
                                        </div>
                                    </div>
                                )}
                            </div>
                        )}

                        <div>
                            <h4 style={{ color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>Solución (Complejidad)</h4>
                            <div className="complexity-badge" style={{ fontSize: '1.2rem' }}>
                                <span dangerouslySetInnerHTML={{ __html: finalComp }} />
                            </div>
                        </div>
                    </div>
                )}

                {activeView === 'info' && (
                    <div className="view-content fade-in">
                        <h3 className="section-title">Análisis</h3>

                        <div style={{ marginBottom: '1.5rem' }}>
                            <h4 style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--accent-secondary)' }}>
                                <CheckCircle size={18} />
                                Explicación del Análisis
                            </h4>
                            <div style={{ background: 'rgba(0,0,0,0.2)', padding: '1.5rem', borderRadius: '8px' }}>
                                {formatExplanation(data.explanation || data.validation_details)}
                            </div>
                        </div>

                        {data.master_theorem_data && (
                            <div>
                                <h4 style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--accent-primary)', marginBottom: '1rem' }}>
                                    <FunctionSquare size={18} />
                                    Datos del Teorema Maestro
                                </h4>

                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
                                    <div className="case-card" style={{ padding: '1rem' }}>
                                        <div style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>Parámetros</div>
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                                            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                                <span>a (subproblemas):</span>
                                                <strong style={{ color: 'var(--accent-primary)' }}>{data.master_theorem_data.a}</strong>
                                            </div>
                                            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                                <span>b (división):</span>
                                                <strong style={{ color: 'var(--accent-primary)' }}>{data.master_theorem_data.b}</strong>
                                            </div>
                                        </div>
                                    </div>

                                    <div className="case-card" style={{ padding: '1rem' }}>
                                        <div style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>Costo de Combinación</div>
                                        <div style={{ fontSize: '1.1rem', fontWeight: 'bold', color: 'var(--accent-secondary)' }}>
                                            f(n) = {data.master_theorem_data.f_n}
                                        </div>
                                    </div>

                                    <div className="case-card" style={{ padding: '1rem', gridColumn: '1 / -1' }}>
                                        <div style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>Resultado</div>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                                            <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#34d399' }}>
                                                {finalComp}
                                            </div>
                                            <div style={{ padding: '0.25rem 0.75rem', background: 'rgba(52, 211, 153, 0.2)', borderRadius: '12px', color: '#34d399', fontSize: '0.9rem' }}>
                                                Caso Aplicado
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                )}

                {activeView === 'trace' && (
                    <div className="view-content fade-in" style={{ padding: 0, display: 'flex', flexDirection: 'column' }}>
                        <div style={{ padding: '1.5rem 1.5rem 0 1.5rem' }}>
                            <h3 className="section-title">Prueba de Escritorio</h3>
                        </div>

                        <div className="trace-table-container">
                            {traceData ? (
                                <table className="trace-table">
                                    <thead>
                                        <tr>
                                            {traceData.headers.map((header, idx) => (
                                                <th key={idx}>{header}</th>
                                            ))}
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {traceData.rows.map((row, rIdx) => (
                                            <tr key={rIdx}>
                                                {row.map((cell, cIdx) => (
                                                    <td key={cIdx}>{cell}</td>
                                                ))}
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            ) : (
                                <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-secondary)' }}>
                                    <p>No se pudo generar la tabla de seguimiento o el formato es incorrecto.</p>
                                    <pre style={{ textAlign: 'left', background: 'rgba(0,0,0,0.2)', padding: '1rem', marginTop: '1rem', fontSize: '0.8rem' }}>
                                        {data.trace_diagram}
                                    </pre>
                                </div>
                            )}
                        </div>
                    </div>
                )}

                {activeView === 'llm_comparison' && (
                    <div className="view-content fade-in">
                        <h3 className="section-title">Verificación con Inteligencia Artificial</h3>

                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginBottom: '2rem' }}>
                            {/* System Calculation */}
                            <div className="case-card" style={{ borderColor: 'var(--accent-primary)' }}>
                                <h4 style={{ color: 'var(--accent-primary)' }}>Cálculo del Sistema</h4>
                                <div className="case-value" style={{ fontSize: '1.5rem' }}>{finalComp}</div>
                                <p>Resultado obtenido mediante análisis estático y conteo de operaciones.</p>
                            </div>

                            {/* LLM Validation */}
                            <div className="case-card" style={{ borderColor: '#a855f7' }}>
                                <h4 style={{ color: '#a855f7', display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <Bot size={16} />
                                    Validación LLM
                                </h4>
                                <div className="case-value" style={{ fontSize: '1.5rem', color: '#d8b4fe' }}>
                                    {data.complexity_validated ? (
                                        <span dangerouslySetInnerHTML={{ __html: data.complexity_validated.match(/[OΘΩThetaOmega]+\s*\(([^)]+)\)/) ? data.complexity_validated.match(/[OΘΩThetaOmega]+\s*\(([^)]+)\)/)[0] : "Ver Texto" }} />
                                    ) : "Pendiente..."}
                                </div>
                                <p>Resultado verificado por el modelo de lenguaje (Gemini).</p>
                            </div>
                        </div>

                        <div style={{ background: 'rgba(168, 85, 247, 0.1)', border: '1px solid rgba(168, 85, 247, 0.3)', borderRadius: '12px', padding: '1.5rem' }}>
                            <h4 style={{ color: '#d8b4fe', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <Info size={18} />
                                Análisis Detallado de la IA
                            </h4>
                            <div style={{ lineHeight: '1.6', color: '#e9d5ff' }}>
                                {(() => {
                                    const text = data.validation_details || data.explanation || "No hay validación disponible.";

                                    try {
                                        // Try to parse as JSON first
                                        // Clean potential markdown code blocks if LLM ignores instruction
                                        const cleanText = text.replace(/```json\n?|\n?```/g, '').trim();
                                        const json = JSON.parse(cleanText);

                                        return (
                                            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                                                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                                                    <div style={{ background: 'rgba(168, 85, 247, 0.2)', padding: '0.5rem 1rem', borderRadius: '8px', border: '1px solid rgba(168, 85, 247, 0.4)' }}>
                                                        <span style={{ fontSize: '0.8rem', color: '#d8b4fe', display: 'block', marginBottom: '0.2rem' }}>Complejidad</span>
                                                        <strong style={{ fontSize: '1.2rem', color: '#fff' }}>{json.complexity}</strong>
                                                    </div>
                                                    <div style={{ flex: 1 }}>
                                                        <span style={{ fontSize: '0.8rem', color: '#94a3b8', display: 'block' }}>Método</span>
                                                        <span style={{ color: '#e2e8f0', fontWeight: '500' }}>{json.method}</span>
                                                    </div>
                                                </div>

                                                <div style={{ background: 'rgba(30, 41, 59, 0.5)', padding: '0.75rem', borderRadius: '8px' }}>
                                                    <span style={{ fontSize: '0.8rem', color: '#94a3b8', display: 'block', marginBottom: '0.5rem' }}>Justificación Clave</span>
                                                    <ul style={{ margin: 0, paddingLeft: '1.2rem', fontSize: '0.9rem', color: '#cbd5e1' }}>
                                                        {json.reasoning.map((item, i) => (
                                                            <li key={i} style={{ marginBottom: '0.25rem' }}>{item}</li>
                                                        ))}
                                                    </ul>
                                                </div>
                                            </div>
                                        );
                                    } catch (e) {
                                        // Fallback to text parsing (previous logic)
                                        const sections = text.split(/\n\s*\n/);

                                        return sections.map((section, idx) => {
                                            const highlighted = section.split(/(\bO\([^)]+\)|\bTheta\([^)]+\)|\bOmega\([^)]+\))/g).map((part, i) =>
                                                part.match(/^(O|Theta|Omega)\(/) ? <strong key={i} style={{ color: '#fff', background: 'rgba(168, 85, 247, 0.3)', padding: '0 4px', borderRadius: '4px' }}>{part}</strong> : part
                                            );

                                            if (section.trim().startsWith('-') || section.trim().startsWith('*')) {
                                                return (
                                                    <ul key={idx} style={{ margin: '0.5rem 0', paddingLeft: '1.5rem' }}>
                                                        {section.split('\n').map((line, liIdx) => (
                                                            <li key={liIdx} style={{ marginBottom: '0.25rem' }}>
                                                                {line.replace(/^[-*]\s*/, '')}
                                                            </li>
                                                        ))}
                                                    </ul>
                                                );
                                            }

                                            return <p key={idx} style={{ marginBottom: '1rem' }}>{highlighted}</p>;
                                        });
                                    }
                                })()}
                            </div>
                        </div>
                    </div>
                )}

                {activeView === 'environments' && (
                    <div className="view-content fade-in">
                        <h3 className="section-title">Ambientes Recursivos</h3>
                        <div style={{ marginTop: '1rem' }}>
                            <RecursionTree data={data.recursion_tree} />
                        </div>
                    </div>
                )}

            </div>
        </div>
    );
};

export default ResultsPanel;
