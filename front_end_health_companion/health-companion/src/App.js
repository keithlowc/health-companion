import React, { Component } from "react";
import "./App.css";
import axios from "axios";
import Biometrics from "./Biometrics/Biometrics.js";
import Chart from "./Charts/LineChart.js";
import HorizontalChart from "./Charts/HorizontalBar.js";

class App extends Component {
  constructor() {
    super();
    this.state = {
      bpm: 0,
      bodyTemp: 0,
      chartData: {},
      chartDataHorizontalBar: {}
    };
  }

  componentWillMount() {
    this.getChartData("http://healthcompanionv1.herokuapp.com/data");
  }

  getChartData = url => {
    axios.get(url).then(response => {
      let all_data = response.data;
      let time_array = [];
      let bpm_array = [];
      let body_temp_array = [];

      let bpm_avg = 0;
      let body_temp_avg = 0;

      for (let i = 0; i < all_data.length; i++) {
        time_array.push(all_data[i]["time"].replace("+00:00", ""));
        bpm_array.push(all_data[i]["bpm"]);
        body_temp_array.push(all_data[i]["bodyTemp"]);
      }
      bpm_avg = this.getAverage(bpm_array);
      body_temp_avg = this.getAverage(body_temp_array);

      this.setState({
        bpm: bpm_avg,
        bodyTemp: body_temp_avg,
        chartData: {
          labels: time_array,
          datasets: [
            {
              label: "Beats Per Minute",
              data: bpm_array,
              backgroundColor: [
                "rgba(255, 99, 132, 0.6)",
                "rgba(54, 162, 235, 0.6)",
                "rgba(255, 206, 86, 0.6)",
                "rgba(75, 192, 192, 0.6)",
                "rgba(153, 102, 255, 0.6)",
                "rgba(255, 159, 64, 0.6)",
                "rgba(255, 99, 132, 0.6)"
              ]
            }
          ]
        },
        chartDataHorizontalBar: {
          labels: time_array,
          datasets: [
            {
              label: "Beats Per Minute",
              data: body_temp_array,
              backgroundColor: [
                "rgba(255, 99, 132, 0.6)",
                "rgba(54, 162, 235, 0.6)",
                "rgba(255, 206, 86, 0.6)",
                "rgba(75, 192, 192, 0.6)",
                "rgba(153, 102, 255, 0.6)",
                "rgba(255, 159, 64, 0.6)",
                "rgba(255, 99, 132, 0.6)"
              ]
            }
          ]
        }
      });
    });
  };

  getAverage = array => {
    let total = 0;
    for (let i = 0; i < array.length; i++) {
      total += array[i];
    }
    total = total / array.length;
    return total;
  };

  handleClick = () => {
    // let url = "http://healthcompanionv1.herokuapp.com/data";
    // this.getBiometrics(url);

    let b = this.getBiometrics();
    console.log(b);
  };

  render() {
    return (
      <div class="container pt-4">
        <button className="button" onClick={this.handleClick}>
          Click Me
        </button>
        <Biometrics bpm={this.state.bpm} bodyTemp={this.state.bodyTemp} />
        <Chart
          chartData={this.state.chartData}
          title_graph="Beats per minutes"
          legendPosition="top"
        />
        <HorizontalChart
          chartData={this.state.chartDataHorizontalBar}
          title_graph="Body Temperature"
          legendPosition="top"
        />
      </div>
    );
  }
}
export default App;
