import React, { Component } from "react";
import { HorizontalBar } from "react-chartjs-2";

class HorizontalChart extends Component {
  constructor(props) {
    super(props);
    this.state = {
      chartData: props.chartData
    };
  }

  static defaultProps = {
    displayTitle: true,
    displayLegend: true,
    legendPosition: "right"
  };

  render() {
    return (
      <div className="chart">
        <HorizontalBar
          data={this.props.chartData}
          width={750}
          height={500}
          options={{
            maintainAspectRatio: false,
            title: {
              display: this.props.displayTitle,
              text: this.props.title_graph,
              fontSize: 25
            },
            legend: {
              display: this.props.displayLegend,
              position: this.props.legendPosition
            }
          }}
        />
      </div>
    );
  }
}

export default HorizontalChart;
