import React, { useState } from 'react';
import ComplexityChart from './ComplexityChart';

const ResultsPanel = ({ data, loading, error }) => {
    const [activeTab, setActiveTab] = useState('summary');

    if (loading) {
        return (
            <div className="glass-panel" style={{ alignItems: 'center', justifyContent: 'center', height: '100%' }}>
                <div className="spinner">Calculando... Por favor espere.</div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="glass-panel" style={{ borderColor: 'var(--accent-danger)' }}>
                <h3 style={{ color: 'var(--accent-danger)' }}>Error</h3>
                <p>{error}</p>
            </div>
        );
    }

    if (!data) {
        return (
            <div className="glass-panel" style={{ alignItems: 'center', justifyContent: 'center', height: '100%', color: 'var(--text-secondary)' }}>
                Ejecuta un análisis para ver los resultados.
            </div>
        );
    }

    // Calculate final complexity for chart
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

    return (
        <div className="results-container" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', height: '100%' }}>
            <div className="glass-panel">
                <h3 style={{ margin: 0, marginBottom: '1rem' }}>Visualización de Complejidad</h3>
                <ComplexityChart complexity={finalComp} />
                <div style={{ textAlign: 'center', marginTop: '10px', fontWeight: 'bold', color: '#DAF7A6' }}>
                    <span dangerouslySetInnerHTML={{ __html: finalComp }} />
                </div>
            </div>

            {/* Debug Dump */}
            <div style={{ padding: '10px', background: '#333', color: '#fff', fontSize: '10px', maxHeight: '100px', overflow: 'auto' }}>
                <strong>DEBUG DATA:</strong> {JSON.stringify(data)}
            </div>

            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', background: 'rgba(30, 41, 59, 0.7)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.1)' }}>
                <div className="tabs" style={{ padding: '10px', borderBottom: '1px solid rgba(255,255,255,0.1)' }}>
                    <button
                        className={`tab ${activeTab === 'summary' ? 'active' : ''}`}
                        onClick={() => setActiveTab('summary')}
                    >
                        Resumen Ejecutivo
                    </button>
                    <button
                        className={`tab ${activeTab === 'logs' ? 'active' : ''}`}
                        onClick={() => setActiveTab('logs')}
                    >
                        Log Completo
                    </button>
                    <button
                        className={`tab ${activeTab === 'trace' ? 'active' : ''}`}
                        onClick={() => setActiveTab('trace')}
                    >
                        Prueba de Escritorio
                    </button>
                </div>

                <div style={{ flex: 1, overflowY: 'auto', padding: '20px' }}>
                    {activeTab === 'summary' && (
                        <div style={{ color: '#f8fafc' }}>
                            <p><strong>📌 ALGORITMO:</strong> {data.algorithm_name || "Desconocido"}</p>
                            <p><strong>✅ COMPLEJIDAD FINAL:</strong> <span dangerouslySetInnerHTML={{ __html: finalComp }} /></p>
                            <p><strong>🧮 Calculado (Raw):</strong> {compCalculated}</p>
                            <p><strong>🤖 Validado (LLM):</strong> {compValidated}</p>

                            <h4 style={{ marginTop: '1rem' }}>📋 ANÁLISIS POR LÍNEAS:</h4>
                            <div className="log-output" style={{ background: 'rgba(0,0,0,0.3)', padding: '10px', borderRadius: '5px' }}>
                                {data.line_by_line && data.line_by_line.length > 0 ? (
                                    data.line_by_line.map((log, idx) => (
                                        <div key={idx} style={{ fontFamily: 'monospace' }}>
                                            Línea {log.line} | {log.cost}
                                        </div>
                                    ))
                                ) : (
                                    <div>No hay detalles línea por línea.</div>
                                )}
                            </div>
                        </div>
                    )}

                    {activeTab === 'logs' && (
                        <div className="log-output">
                            <pre>{JSON.stringify(data, null, 2)}</pre>
                        </div>
                    )}

                    {activeTab === 'trace' && (
                        <div className="log-output">
                            <pre>{data.trace_diagram || "No hay diagrama de seguimiento disponible."}</pre>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default ResultsPanel;
