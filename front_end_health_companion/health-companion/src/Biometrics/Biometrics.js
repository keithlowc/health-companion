import React, { Component } from "react";
import "./Biometrics.css";

class Biometrics extends Component {
  state = {};

  render() {
    return (
      <div class="col-lg-12">
        <img class="Logo_image" src={this.props.img} />
        <h1>
          {this.props.title}{" "}
          <span class="badge badge-success">{this.props.data}</span>
        </h1>
      </div>
    );
  }
}

export default Biometrics;
