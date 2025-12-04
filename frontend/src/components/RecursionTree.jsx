import React from 'react';

const TreeNode = ({ node }) => {
    if (!node) return null;

    // Parse label to extract function name and arguments
    // Expected format: "Func(arg1, arg2, ...)"
    const parseLabel = (label) => {
        if (!label) return { name: 'Unknown', args: [] };
        const match = label.match(/^([^(]+)\((.*)\)$/);
        if (!match) return { name: label, args: [] };

        const name = match[1];
        const argsStr = match[2];
        // Split by comma, but respect nested parenthesis if any (simple split for now)
        const args = argsStr.split(',').map(arg => arg.trim()).filter(a => a);
        return { name, args };
    };

    const { name, args } = parseLabel(node.label);

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: '0 25px' }}>
            {/* Node Card (Stack Frame Style) */}
            <div style={{
                border: '1px solid rgba(59, 130, 246, 0.4)', // Blue border
                borderRadius: '6px',
                background: 'rgba(15, 23, 42, 0.9)', // Dark background
                minWidth: '160px',
                boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.5)',
                marginBottom: '40px', // Increased vertical spacing
                position: 'relative',
                zIndex: 2,
                overflow: 'hidden'
            }}>
                {/* Header: Function Name */}
                <div style={{
                    background: 'rgba(59, 130, 246, 0.2)',
                    padding: '6px 10px',
                    borderBottom: '1px solid rgba(59, 130, 246, 0.2)',
                    fontWeight: 'bold',
                    color: '#60a5fa',
                    fontSize: '0.9rem',
                    textAlign: 'center',
                    position: 'relative'
                }}>
                    {/* Execution Order Badge */}
                    {node.execution_order && (
                        <div style={{
                            position: 'absolute',
                            top: '50%',
                            left: '10px',
                            transform: 'translateY(-50%)',
                            background: '#ef4444', // Red color for visibility
                            color: 'white',
                            borderRadius: '50%',
                            width: '20px',
                            height: '20px',
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                            fontSize: '0.7rem',
                            fontWeight: 'bold',
                            boxShadow: '0 2px 4px rgba(0,0,0,0.3)'
                        }}>
                            {node.execution_order}
                        </div>
                    )}
                    {name}
                </div>

                {/* Body: Arguments Table */}
                <div style={{ padding: '8px' }}>
                    {args.length > 0 ? (
                        <table style={{ width: '100%', fontSize: '0.8rem', borderCollapse: 'collapse' }}>
                            <tbody>
                                {args.map((arg, idx) => (
                                    <tr key={idx}>
                                        <td style={{ color: '#94a3b8', paddingRight: '8px', textAlign: 'right', width: '40%' }}>arg{idx + 1}:</td>
                                        <td style={{ color: '#e2e8f0', textAlign: 'left' }}>{arg}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    ) : (
                        <div style={{ fontSize: '0.8rem', color: '#94a3b8', textAlign: 'center' }}>Sin argumentos</div>
                    )}
                </div>

                {/* Footer: Return Value */}
                {node.result && (
                    <div style={{
                        borderTop: '1px solid rgba(255, 255, 255, 0.1)',
                        padding: '6px 10px',
                        background: 'rgba(255, 255, 255, 0.03)',
                        fontSize: '0.85rem',
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center'
                    }}>
                        <span style={{ color: '#94a3b8' }}>Retorna:</span>
                        <span style={{ color: '#34d399', fontWeight: 'bold' }}>{node.result}</span>
                    </div>
                )}

                {/* Vertical line down from parent */}
                {node.children && node.children.length > 0 && (
                    <div style={{
                        position: 'absolute',
                        bottom: '-40px', // Extend further down to match marginBottom
                        left: '50%',
                        transform: 'translateX(-50%)',
                        width: '2px',
                        height: '40px',
                        background: 'rgba(255, 255, 255, 0.3)',
                        display: 'flex',
                        justifyContent: 'center',
                        alignItems: 'flex-end'
                    }}>
                        {/* Down Arrow */}
                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ marginBottom: '-4px' }}>
                            <path d="M5 6L0 0H10L5 6Z" fill="rgba(255, 255, 255, 0.3)" />
                        </svg>
                    </div>
                )}
            </div>

            {/* Children Container */}
            {node.children && node.children.length > 0 && (
                <div style={{ display: 'flex', position: 'relative', paddingTop: '40px' }}>

                    {/* Horizontal Bar connecting children */}
                    {node.children.length > 1 && (
                        <div style={{
                            position: 'absolute',
                            top: 0,
                            left: '80px', // Approx half of minWidth
                            right: '80px',
                            height: '2px',
                            background: 'rgba(255, 255, 255, 0.3)'
                        }} />
                    )}

                    {node.children.map((child, index) => (
                        <div key={index} style={{ position: 'relative', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                            {/* Vertical line up from child to horizontal bar */}
                            <div style={{
                                position: 'absolute',
                                top: '-40px',
                                left: '50%',
                                transform: 'translateX(-50%)',
                                width: '2px',
                                height: '40px',
                                background: 'rgba(255, 255, 255, 0.3)'
                            }} />
                            <TreeNode node={child} />
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

const RecursionTree = ({ data }) => {
    if (!data || !data.root) {
        return (
            <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-secondary)' }}>
                No hay datos de árbol de recursión disponibles.
            </div>
        );
    }

    return (
        <div style={{
            overflowX: 'auto',
            padding: '2rem',
            minHeight: '400px'
        }}>
            <div style={{
                display: 'flex',
                justifyContent: 'center',
                minWidth: '100%',
                width: 'fit-content'
            }}>
                <TreeNode node={data.root} />
            </div>
        </div>
    );
};

export default RecursionTree;
