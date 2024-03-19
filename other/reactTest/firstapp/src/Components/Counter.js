import React from "react";
import { useState } from "react";
export const Counter = () => {
    const [counter, setCounter] = useState(0);
    return (
        <div className="counter">
            <h1>Counter</h1>
            <button onClick={() => setCounter((prevCount) => prevCount - 1)}>
                -
            </button>
            <h1>{counter}</h1>
            <button onClick={() => setCounter((prevCount) => prevCount + 1)}>
                +
            </button>
        </div>
    );
};
