import React, { Component } from "react";
import "./Biometrics.css";

class Biometrics extends Component {
  state = {};

  render() {
    return (
      <div class="col-lg-12 pt-4">
        <img class="Logo_image" alt="jsx-a11y/alt-text" src={this.props.img} />
        <h1 class="pt-4">
          {this.props.title}{" "}
          <span class="badge badge-success">{this.props.data}</span>
        </h1>
        <b>
          Status: <span class="badge badge-primary">{this.props.status}</span>
        </b>
      </div>
    );
  }
}

export default Biometrics;
