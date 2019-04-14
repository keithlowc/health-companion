import React, { Component } from "react";
import "./App.css";
import axios from "axios";
import Biometrics from "./Biometrics/Biometrics.js";
import Chart from "./Charts/LineChart.js";
import HorizontalChart from "./Charts/HorizontalBar.js";
import { isAbsolute } from "path";

class App extends Component {
  constructor() {
    super();

    this.state = {
      bpm: 0,
      bodyTemp: 0,
      chartData: {},
      chartDataHorizontalBar: {},
      interval: 0,
      status: "Null",
      size_val: 10
    };
  }

  componentWillMount() {
    this.getChartData("http://healthcompanionv1.herokuapp.com/data");
  }

  componentDidMount() {
    this.interval = setInterval(
      () => this.getChartData("http://healthcompanionv1.herokuapp.com/data"),
      5000
    );
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  getChartData = url => {
    axios.get(url).then(response => {
      let all_data = response.data;
      let time_array = [];
      let bpm_array = [];
      let body_temp_array = [];

      let time = "";

      let size = all_data.length;

      let wanted = 20;
      let index = size - wanted;

      for (let i = index; i < all_data.length; i++) {
        time = all_data[i]["time"].split(".")[0].replace("T", " ");
        time_array.push(time);
        bpm_array.push(all_data[i]["bpm"]);
        body_temp_array.push(all_data[i]["bodyTemp"]);
      }

      let bpm_avg = this.getAverage(bpm_array);
      let body_temp_avg = this.getAverage(body_temp_array);

      let new_status = this.calculateStatus(bpm_avg, body_temp_avg);
      console.log(new_status);

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
                "rgba(255, 99, 132, 0.6)",
                "rgba(255, 99, 132, 0.6)",
                "rgba(54, 162, 235, 0.6)",
                "rgba(255, 206, 86, 0.6)",
                "rgba(75, 192, 192, 0.6)",
                "rgba(153, 102, 255, 0.6)",
                "rgba(255, 159, 64, 0.6)",
                "rgba(255, 99, 132, 0.6)",
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
                "rgba(255, 99, 132, 0.6)",
                "rgba(255, 99, 132, 0.6)",
                "rgba(54, 162, 235, 0.6)",
                "rgba(255, 206, 86, 0.6)",
                "rgba(75, 192, 192, 0.6)",
                "rgba(153, 102, 255, 0.6)",
                "rgba(255, 159, 64, 0.6)",
                "rgba(255, 99, 132, 0.6)",
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
        status: new_status,
        size_val: size
      });
    });
  };

  getAverage = array => {
    let total = 0;
    for (let i = 0; i < array.length; i++) {
      total += array[i];
    }
    total = total / array.length;
    return total.toFixed(0);
  };

  calculateStatus = (bpm, bodyTemp) => {
    let status = "";
    if (bpm >= 60 && bpm <= 100 && bodyTemp >= 95 && bodyTemp <= 99) {
      status = "Good";
      return status;
    } else if (bpm < 60 && bodyTemp < 95) {
      status = "Bad";
      return status;
    } else {
      status = "Normal";
      return status;
    }
  };

  render() {
    return (
      <div class="container pt-4">
        <div class="row pt-4">
          <div class="col-md-4 text-center">
            <div class="row ">
              <Biometrics
                data={this.state.bpm}
                img="https://cdn4.iconfinder.com/data/icons/medical-32/512/medic2-512.png"
                title="Bpm: "
              />
            </div>
          </div>

          <div class="col-md-4 text-center">
            <Biometrics img="https://www.shareicon.net/data/512x512/2016/08/18/813844_people_512x512.png" />
            <h1>Welcome Keith !</h1>
            <p>
              Status:{" "}
              <span class="badge badge-primary">{this.state.status}</span>
            </p>
          </div>
          <div class="col-md-4 text-center">
            <Biometrics
              data={this.state.bodyTemp}
              img="http://icons.iconarchive.com/icons/google/noto-emoji-travel-places/256/42650-thermometer-icon.png"
              title="Temp (F): "
            />
          </div>
        </div>

        <div class="row border-top mt-4">
          <div class="col-lg-12 ">
            <Chart
              chartData={this.state.chartData}
              title_graph="Beats Per Minute"
              legendPosition="top"
            />
          </div>
        </div>

        <div class="row border-top mt-4">
          <div class="col-lg-12 ">
            <HorizontalChart
              chartData={this.state.chartDataHorizontalBar}
              title_graph="Body Temperature"
              legendPosition="top"
            />
          </div>
        </div>
      </div>
    );
  }
}
export default App;
