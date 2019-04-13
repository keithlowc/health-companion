import React from "react";

const biometrics = props => {
  return (
    <div>
      <p>Your Average Bpm is: {props.bpm}</p>
      <p>Your Average Body Temp is: {props.bodyTemp}</p>
      <p>{props.children}</p>
    </div>
  );
};

export default biometrics;
