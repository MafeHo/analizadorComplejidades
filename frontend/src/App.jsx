import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import axios from 'axios';
import { Play, Upload, Activity, GitGraph } from 'lucide-react';
import ResultsPanel from './components/ResultsPanel';
import './App.css';

function App() {
  const [code, setCode] = useState(`// Torres de Hanoi
HANOI(n)
begin
    If (n = 1) then
    begin
        HANOI <- 1;
    end
    else
    begin
        HANOI <- HANOI(n-1) + 1 + HANOI(n-1);
    end;
end`);
  const [translateMode, setTranslateMode] = useState(false);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    setLoading(true);
    setError(null);
    setResults(null);
    try {
      const response = await axios.post('http://localhost:8000/analyze', {
        code,
        translate: translateMode
      });
      setResults(response.data);
    } catch (err) {
      setError(err.message || 'Error al conectar con el servidor');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => setCode(e.target.result);
      reader.readAsText(file);
    }
  };

  return (
    <div className="app-container">
      <div className="sidebar">
        <div style={{ marginBottom: '1rem' }}>
          <h2 style={{ margin: 0, color: 'var(--accent-primary)' }}>Analizador</h2>
          <h2 style={{ margin: 0, color: 'white' }}>Algorítmico</h2>
        </div>

        <div className="input-group">
          <label className="btn btn-primary" style={{ cursor: 'pointer' }}>
            <Upload size={18} />
            Cargar Archivo
            <input type="file" hidden onChange={handleFileUpload} />
          </label>
        </div>

        <div className="input-group" style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
          <span className="label">Editor de Código:</span>
          <div style={{ flex: 1, border: '1px solid var(--glass-border)', borderRadius: '8px', overflow: 'hidden' }}>
            <Editor
              height="100%"
              defaultLanguage="plaintext"
              theme="vs-dark"
              value={code}
              onChange={(value) => setCode(value)}
              options={{
                minimap: { enabled: false },
                fontSize: 14,
                scrollBeyondLastLine: false,
                automaticLayout: true
              }}
            />
          </div>
        </div>

        <div className="switch-container" onClick={() => setTranslateMode(!translateMode)}>
          <div className={`switch-input ${translateMode ? 'checked' : ''}`} style={{ background: translateMode ? 'var(--accent-primary)' : 'var(--bg-tertiary)' }}></div>
          <span className="label" style={{ margin: 0, color: 'white' }}>Traducir Lenguaje Natural</span>
        </div>

        <button
          className="btn btn-success"
          onClick={handleAnalyze}
          disabled={loading}
        >
          <Play size={18} />
          {loading ? 'Analizando...' : 'EJECUTAR ANÁLISIS'}
        </button>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          <button className="btn btn-danger" onClick={() => alert("Funcionalidad de visualización de pila pendiente de migración")}>
            <Activity size={18} />
            Ver Pila Recursión
          </button>
          <button className="btn btn-primary" style={{ backgroundColor: '#10b981' }} onClick={() => alert("Funcionalidad de visualización de árbol pendiente de migración")}>
            <GitGraph size={18} />
            Visualizar Árbol
          </button>
        </div>
      </div>

      <div className="main-content">
        <ResultsPanel data={results} loading={loading} error={error} />
      </div>
    </div>
  );
}

export default App;
