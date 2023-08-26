const countries = ["India", "Nepal", "Germany", "Finland"];



app.get("/api/countries", (req, res) => {
    const rows = 3;
    const cols = 3;
    const result = [];
    for (let i = 0; i < rows; i++) {
        const row = [];
        for (let j = 0; j < cols; j++) {
            const randomIndex = Math.floor(Math.random() * countries.length);
            row.push(countries[randomIndex]);
        }
        result.push(row);
    }
    res.send(result);
});




import React, { useState, useEffect } from "react";
import axios from "axios";

const TagControl = () => {
    const [matrix, setMatrix] = useState([]);
    const [ranks, setRanks] = useState({ India: 0, Nepal: 0 });

    useEffect(() => {
        axios.get("/api/countries").then((response) => {
            setMatrix(response.data);
        });
    }, []);

    useEffect(() => {
        const newRanks = { India: 0, Nepal: 0 };
        matrix.forEach((row) => {
            let currentCountry = row[0];
            let currentCount = 1;
            for (let i = 1; i < row.length; i++) {
                if (row[i] === currentCountry) {
                    currentCount++;
                    if (currentCount > newRanks[currentCountry]) {
                        newRanks[currentCountry] = currentCount;
                    }
                } else {
                    currentCountry = row[i];
                    currentCount = 1;
                }
            }
        });
        setRanks(newRanks);
    }, [matrix]);

    return (
        <>
            <div className="matrix">
                {matrix.map((row, rowIndex) => (
                    <div className="row" key={rowIndex}>
                        {row.map((country, colIndex) => (
                            <div className="cell" key={`${rowIndex}-${colIndex}`}>
                                {country}
                            </div>
                        ))}
                    </div>
                ))}
            </div>
            <div className="ranks">
                <div className="rank">
                    India: {ranks.India}
                </div>
                <div className="rank">
                    Nepal: {ranks.Nepal}
                </div>
            </div>
        </>
    );
};

export default TagControl;


.matrix {
    display: flex;
    flex - direction: column;
    border: 1px solid #ccc;
    margin - bottom: 20px;
}
  
  .row {
    display: flex;
    flex - direction: row;
}
  
  .cell {
    flex: 1;
    border: 1px
