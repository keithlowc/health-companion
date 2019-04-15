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
      chartDataHorizontalBar: {},
      interval: 0,
      overall_status: "Null",
      bpm_status: "Null",
      bodyTemp_status: "Null",
      data_size: 0
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
    axios
      .get(url)
      .then(response => {
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
        let bpm_stats = this.calculate_individual_stat_bpm(bpm_avg);
        let bodyTemp_stat = this.calculate_individual_stat_bodyTemp(
          body_temp_avg
        );

        console.log("This is the current status: ", new_status);

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
          overall_status: new_status,
          bpm_status: bpm_stats,
          bodyTemp_status: bodyTemp_stat,
          data_size: size
        });
      })
      .catch(error => console.log(error));
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

  calculate_individual_stat_bpm = bpm => {
    let bpm_status = "";
    if (bpm >= 60 && bpm <= 100) {
      bpm_status = "Normal Range";
    } else if (bpm > 110) {
      bpm_status = "Too High";
    } else if (bpm < 60) {
      bpm_status = "Too Low";
    } else {
      bpm_status = "Null";
    }
    return bpm_status;
  };

  calculate_individual_stat_bodyTemp = bodyTemp => {
    let bodyTemp_status = "";

    if (bodyTemp >= 95 && bodyTemp <= 99) {
      bodyTemp_status = "Normal Range";
    } else if (bodyTemp > 99) {
      bodyTemp_status = "Too High";
    } else if (bodyTemp < 95) {
      bodyTemp_status = "Too Low";
    } else {
      bodyTemp_status = "Null";
    }
    return bodyTemp_status;
  };

  delete_data = () => {
    console.log("Delete was pressed!");
    let val_to_delete = this.state.data_size;
    val_to_delete--;
    console.log("The next id to delete: ", val_to_delete);
    let url =
      "http://healthcompanionv1.herokuapp.com/data" +
      "/" +
      String(val_to_delete);
    axios.delete(url);
    console.log("The url just deleted: ", url);
    alert("Record number #" + val_to_delete + ". Was deleted!");
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
                status={this.state.bpm_status}
              />
            </div>
          </div>

          <div class="col-md-4 text-center">
            <Biometrics
              img="https://www.shareicon.net/data/512x512/2016/08/18/813844_people_512x512.png"
              title="Welcome Keith !"
              status={this.state.overall_status}
            />
          </div>
          <div class="col-md-4 text-center">
            <Biometrics
              data={this.state.bodyTemp}
              img="http://icons.iconarchive.com/icons/google/noto-emoji-travel-places/256/42650-thermometer-icon.png"
              title="Temp (F): "
              status={this.state.bodyTemp_status}
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
        <div class="row mt-4 mb-4">
          <div class="col-md-4" />
          <div class="col-md-4 text-center">
            <button onClick={this.delete_data} class="btn btn-danger">
              Reset Once
            </button>
          </div>
          <div class="col-md-4" />
        </div>
      </div>
    );
  }
}
export default App;
