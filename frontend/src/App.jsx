import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import axios from 'axios';
import { Play, Upload, FileCode, Network } from 'lucide-react';
import ResultsPanel from './components/ResultsPanel';
import NaturalLanguageInput from './components/NaturalLanguageInput';
import TreeModal from './components/TreeModal';
import './App.css';
import ComplexityChart from './components/ComplexityChart';



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
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const [showTreeModal, setShowTreeModal] = useState(false);

  const handleAnalyze = async () => {
    setLoading(true);
    setError(null);
    setResults(null);
    try {
      const response = await axios.post('http://localhost:8000/analyze', {
        code,
        translate: false
      });

      const data = response.data;

      // Check for API errors in the response content
      if (data.complexity_validated && typeof data.complexity_validated === 'string' && data.complexity_validated.includes("Error API")) {
        // Extract the error message
        setError(data.complexity_validated);
        setResults(null);
      } else if (data.trace_diagram && typeof data.trace_diagram === 'string' && data.trace_diagram.includes("Error API")) {
        setError(data.trace_diagram);
        setResults(null);
      } else {
        setResults(data);
      }

    } catch (err) {
      setError(err.message || 'Error al conectar con el servidor');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleTranslate = async (text) => {
    setLoading(true);
    setError(null);
    try {
      const res = await axios.post('http://localhost:8000/analyze', {
        code: text,
        translate: true
      });

      if (res.data && res.data.pseudocode) {
        setCode(res.data.pseudocode);
      } else {
        console.warn("Backend didn't return translated code. Using input.");
        setCode(text);
      }

      // Check for API errors here too
      if (res.data.complexity_validated && typeof res.data.complexity_validated === 'string' && res.data.complexity_validated.includes("Error API")) {
        setError(res.data.complexity_validated);
        setResults(null);
      } else {
        setResults(res.data);
      }

    } catch (err) {
      setError("Error al traducir/analizar: " + err.message);
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

  const TEST_CODES = {
    "Burbuja": `// Algoritmo de Ordenamiento Burbuja
BURBUJA(A, n)
begin
    for i <- 1 to n-1 do
    begin
        for j <- 1 to n-i do
        begin
            If (A[j] > A[j+1]) then
            begin
                temp <- A[j];
                A[j] <- A[j+1];
                A[j+1] <- temp;
            end;
        end;
    end;
end`,
    "Busqueda Seq": `// Busqueda Secuencial
BUSQUEDA(A, n, x)
begin
    i <- 1;
    encontrado <- 0;
    while (i <= n) do
    begin
        If (A[i] = x) then
        begin
            encontrado <- 1;
            i <- n + 1;
        end
        else
        begin
            i <- i + 1;
        end;
    end;
end`,
    "Factorial": `// Algoritmo Factorial Recursivo
FACTORIAL(n)
begin
    If (n = 0) then
    begin
        FACTORIAL <- 1;
    end
    else
    begin
        FACTORIAL <- n * FACTORIAL(n-1);
    end;
end`,
    "Fibonacci": `Fibonacci(n)
begin
    If (n <= 1) then
    begin
        return n;
    end
    else
    begin
        return Fibonacci(n-1) + Fibonacci(n-2);
    end;
end`,
    "Hanoi": `// Torres de Hanoi
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
end`,
    "Merge Sort": `// Algoritmo MergeSort
MERGE_SORT(A, n)
begin
    If (n > 1) then
    begin
        mitad <- n / 2;
        CALL MERGE_SORT(A, mitad);
        CALL MERGE_SORT(A, mitad);
        for i <- 1 to n do
        begin
            temp <- A[i];
        end;
    end;
end`,
    "Suma Arreglo": `// Suma Arreglo
ALGORITMO_SUMA(A[n])
begin
    total <- 0;
    for i <- 1 to n do 
    begin
        total <- total + A[i]; 
    end;
    end;
end`,
    "Suma Gauss": `// Suma Gauss
SUMA_GAUSS(n)
begin
    suma <- 0;
    for i <- 1 to n do
    begin
        suma <- suma + i;
    end;
    SUMA_GAUSS <- suma;
end`,
    "Matriz Rec": `MatrizRecursiva(n)
begin
    If (n > 1) then
    begin
        mitad <- n / 2;
        CALL MatrizRecursiva(mitad);
        CALL MatrizRecursiva(mitad);
        CALL MatrizRecursiva(mitad);
        CALL MatrizRecursiva(mitad);
        CALL MatrizRecursiva(mitad);
        CALL MatrizRecursiva(mitad);
        CALL MatrizRecursiva(mitad);
        CALL MatrizRecursiva(mitad);
        for i <- 1 to n do begin
            for j <- 1 to n do begin
                suma <- 1;
            end;
        end;
    end
end`,
    "Divide 4": `DivideEnCuatro(n)
begin
    If (n > 1) then
    begin
        cuarto <- n / 4;
        CALL DivideEnCuatro(cuarto);
        CALL DivideEnCuatro(cuarto);
        CALL DivideEnCuatro(cuarto);
        CALL DivideEnCuatro(cuarto);
        i <- 0;
        while (i < n) do
        begin
            i <- i + 1;
        end;
    end;
end`
  };

  // Calculate final complexity for chart (Side Panel)
  let finalComp = "O(n)";
  if (results) {
    const compValidated = results.complexity_validated || "";
    const compCalculated = results.complexity_calculated || "";
    const match = compValidated.match(/[OΘΩThetaOmega]+\s*\(([^)]+)\)/);
    if (match) {
      finalComp = match[0];
    } else if (compCalculated.includes("2^n") || compCalculated.includes("2**n")) {
      finalComp = "O(2^n)";
    } else if (compCalculated !== "Desconocida") {
      finalComp = compCalculated;
    }
  }

  return (
    <div className="app-container">
      {/* Header */}
      <header className="app-header">
        <h1>Analizador de Complejidad</h1>
      </header>

      {/* 1. Natural Language Input */}
      <section className="input-section">
        <NaturalLanguageInput onTranslate={handleTranslate} loading={loading} />
      </section>

      {/* 2. Test Buttons Section */}
      <section className="test-section">
        <h3 style={{ margin: '0 0 1rem 0', color: 'var(--text-secondary)', fontSize: '1rem' }}>Pseudocódigos de Prueba</h3>
        <div className="test-buttons-grid">
          {Object.entries(TEST_CODES).map(([name, codeStr]) => (
            <button key={name} className="btn-test" onClick={() => setCode(codeStr)}>
              {name}
            </button>
          ))}
        </div>
      </section>

      {/* 3. Editor & Chart Row */}
      <section className="editor-row">
        {/* Left: Editor */}
        <div className="editor-wrapper glass-panel">
          <div className="toolbar" style={{ padding: '8px', borderBottom: '1px solid var(--glass-border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'rgba(0,0,0,0.2)' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <FileCode size={16} color="var(--accent-primary)" />
              <span style={{ fontSize: '0.9rem', fontWeight: 600 }}>Editor de Pseudocódigo</span>
            </div>
            <div style={{ display: 'flex', gap: '8px' }}>
              <label className="btn-icon" title="Subir Archivo">
                <Upload size={16} />
                <input type="file" onChange={handleFileUpload} style={{ display: 'none' }} />
              </label>
            </div>
          </div>
          <div style={{ flex: 1, minHeight: 0 }}>
            <Editor
              height="100%" // Fill the container
              defaultLanguage="plaintext"
              value={code}
              onChange={(value) => setCode(value)}
              theme="vs-dark"
              options={{
                minimap: { enabled: false },
                fontSize: 14,
                lineNumbers: 'on',
                scrollBeyondLastLine: false,
                automaticLayout: true,
                padding: { top: 10, bottom: 10 },
                fontFamily: "'JetBrains Mono', monospace",
                backgroundColor: 'transparent',
              }}
            />
          </div>
        </div>

        {/* Right: Complexity Chart (Always Visible) */}
        <div className="chart-side-panel glass-panel">
          <div style={{ padding: '1rem', borderBottom: '1px solid var(--glass-border)', background: 'rgba(0,0,0,0.2)' }}>
            <h3 style={{ margin: 0, fontSize: '1rem', color: 'var(--text-primary)' }}>Complejidad Asintótica</h3>
          </div>
          <div style={{ padding: '1rem', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1 }}>
            {results ? (
              <>
                <div className="complexity-badge" style={{ fontSize: '1.2rem', padding: '0.5rem 1rem', marginBottom: '1rem' }}>
                  <span dangerouslySetInnerHTML={{ __html: finalComp }} />
                </div>
                <div style={{ width: '100%', height: '200px' }}>
                  <ComplexityChart complexity={finalComp} />
                </div>
              </>
            ) : (
              <div style={{ color: 'var(--text-secondary)', textAlign: 'center', fontSize: '0.9rem' }}>
                Ejecuta un análisis para ver la gráfica.
              </div>
            )}
          </div>
        </div>
      </section>

      {/* 4. Action Button */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', margin: '1rem 0' }}>
        <button
          className="btn btn-primary"
          onClick={handleAnalyze}
          disabled={loading}
          style={{ padding: '0.8rem 3rem', fontSize: '1.1rem' }}
        >
          {loading ? (
            <>
              <div className="spinner" style={{ width: '20px', height: '20px', borderTopColor: 'white' }}></div>
              Analizando...
            </>
          ) : (
            <>
              <Play size={20} />
              Analizar Complejidad
            </>
          )}
        </button>

        {results && results.master_theorem_data && (
          <button
            className="btn btn-secondary"
            onClick={() => setShowTreeModal(true)}
            style={{ padding: '0.8rem 2rem', fontSize: '1.1rem', backgroundColor: '#2b2b2b', border: '1px solid #444', display: 'flex', alignItems: 'center', gap: '8px' }}
          >
            <Network size={20} color="#33C1FF" />
            Visualizar Árbol
          </button>
        )}
      </div>

      {/* 5. Results Panel (Full Width) */}
      <section className="results-section-full">
        <ResultsPanel data={results} loading={loading} error={error} />
      </section>

      {/* Modals */}
      <TreeModal isOpen={showTreeModal} onClose={() => setShowTreeModal(false)} data={results} />
    </div>
  );
}

export default App;
