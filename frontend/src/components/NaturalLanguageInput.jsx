import React, { useState } from 'react';
import { ArrowRight, Sparkles } from 'lucide-react';

const NaturalLanguageInput = ({ onTranslate, loading }) => {
    const [input, setInput] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (input.trim()) {
            onTranslate(input);
        }
    };

    return (
        <div className="glass-panel" style={{ padding: '1.5rem', marginBottom: '1.5rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
                <Sparkles size={20} color="var(--accent-secondary)" />
                <h3 style={{ margin: 0, fontSize: '1.1rem', color: 'var(--text-primary)' }}>Generador de Pseudocódigo</h3>
            </div>

            <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '1rem' }}>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Describe tu algoritmo aquí (ej: 'Calcula el factorial de n de forma recursiva')"
                    className="nl-input"
                    style={{
                        flex: 1,
                        background: 'rgba(0,0,0,0.2)',
                        border: '1px solid var(--glass-border)',
                        borderRadius: '8px',
                        padding: '0.75rem 1rem',
                        color: 'white',
                        fontSize: '1rem',
                        outline: 'none'
                    }}
                />
                <button
                    type="submit"
                    className="btn btn-primary"
                    disabled={loading || !input.trim()}
                    style={{ minWidth: '120px' }}
                >
                    {loading ? 'Generando...' : (
                        <>
                            Generar <ArrowRight size={16} />
                        </>
                    )}
                </button>
            </form>
        </div>
    );
};

export default NaturalLanguageInput;
