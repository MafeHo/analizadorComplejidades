import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const ComplexityChart = ({ complexity }) => {
    const generateData = () => {
        const data = [];
        const c_lower = complexity.toLowerCase();

        for (let n = 1; n <= 12; n++) {
            let val = n;
            if (c_lower.includes("2^n") || c_lower.includes("2**n") || c_lower.includes("exponencial")) {
                val = Math.pow(2, n);
            } else if (c_lower.includes("phi^n") || c_lower.includes("φ^n") || c_lower.includes("1.618^n")) {
                val = Math.pow(1.618, n);
            } else if (c_lower.includes("n^3")) {
                val = Math.pow(n, 3);
            } else if (c_lower.includes("n^2")) {
                val = Math.pow(n, 2);
            } else if (c_lower.includes("nlog")) {
                val = n * Math.log2(n);
            } else if (c_lower.includes("log")) {
                val = Math.log2(n);
            } else if (c_lower.includes("1") && !c_lower.includes("n")) {
                val = 1;
            }

            data.push({ n, value: val });
        }
        return data;
    };

    const data = generateData();

    // Determine color based on complexity
    let color = '#DAF7A6'; // Linear
    const c_lower = complexity.toLowerCase();
    if (c_lower.includes("2^n") || c_lower.includes("exponencial") || c_lower.includes("phi^n") || c_lower.includes("φ^n") || c_lower.includes("1.618^n")) color = '#FF33A8';
    else if (c_lower.includes("n^3")) color = '#C70039';
    else if (c_lower.includes("n^2")) color = '#FF5733';
    else if (c_lower.includes("nlog")) color = '#33FF57';
    else if (c_lower.includes("log")) color = '#33C1FF';
    else if (c_lower.includes("1") && !c_lower.includes("n")) color = '#FFC300';

    return (
        <div style={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column' }}>
            <div style={{ flex: 1, minHeight: 0 }}>
                <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                        <CartesianGrid stroke="#444" strokeDasharray="3 3" />
                        <XAxis dataKey="n" stroke="#888" />
                        <YAxis stroke="#888" />
                        <Tooltip
                            contentStyle={{ backgroundColor: '#1e293b', border: 'none', borderRadius: '8px', color: '#fff' }}
                            itemStyle={{ color: color }}
                        />
                        <Line type="monotone" dataKey="value" stroke={color} strokeWidth={3} dot={{ r: 4 }} />
                    </LineChart>
                </ResponsiveContainer>
            </div>
            <div style={{ textAlign: 'center', color: color, marginTop: '10px', fontWeight: 'bold' }}>
                {complexity}
            </div>
        </div>
    );
};

export default ComplexityChart;
