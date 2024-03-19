import React from "react";

export const Person = (props) =>
{
    return (
    <>
    <h1>Name: {props.name}</h1>
    <h2>Surname: {props.surName}</h2>
    <h3>Age: {props.age}</h3>
    </>
    );
};
