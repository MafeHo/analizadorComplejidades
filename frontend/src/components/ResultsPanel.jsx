import React, { useState } from 'react';
import { Activity, List, BarChart2, AlertCircle, CheckCircle, FunctionSquare, Info, Table } from 'lucide-react';

const ResultsPanel = ({ data, loading, error }) => {
    const [activeView, setActiveView] = useState('lines'); // lines, cases, recurrence, info, trace

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
                    Recurrencia
                </button>
                <button
                    className={`nav-btn ${activeView === 'info' ? 'active' : ''}`}
                    onClick={() => setActiveView('info')}
                >
                    <Info size={18} />
                    Info Extra
                </button>
                <button
                    className={`nav-btn ${activeView === 'trace' ? 'active' : ''}`}
                    onClick={() => setActiveView('trace')}
                >
                    <Table size={18} />
                    Prueba
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
                        <h3 className="section-title">Ecuación de Recurrencia</h3>

                        <div style={{ marginBottom: '2rem' }}>
                            <h4 style={{ color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>Tipo de Algoritmo</h4>
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
                        <h3 className="section-title">Información Adicional</h3>

                        <div style={{ marginBottom: '1.5rem' }}>
                            <h4 style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--accent-secondary)' }}>
                                <CheckCircle size={18} />
                                Explicación del Análisis
                            </h4>
                            <div style={{ background: 'rgba(0,0,0,0.2)', padding: '1rem', borderRadius: '8px', lineHeight: '1.6', fontSize: '0.95rem' }}>
                                {data.explanation || data.validation_details || "No hay explicación detallada disponible."}
                            </div>
                        </div>

                        {data.master_theorem_data && (
                            <div>
                                <h4 style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--accent-primary)' }}>
                                    <FunctionSquare size={18} />
                                    Datos del Teorema Maestro
                                </h4>
                                <pre style={{ background: 'rgba(0,0,0,0.2)', padding: '1rem', borderRadius: '8px', overflowX: 'auto' }}>
                                    {JSON.stringify(data.master_theorem_data, null, 2)}
                                </pre>
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

            </div>
        </div>
    );
};

export default ResultsPanel;
