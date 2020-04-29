import React, {Component} from 'react';
import {Bar, Line, Pie} from 'react-chartjs-2';

class Chart extends Component{

    constructor(props){
        super(props);
        this.state = {
            chartData:{
                labels: ['California', 'Washington', 'Carolina', 'New York', 'Oregon', 'Colorado',
            'Nevada'],
            datasets:[
                {
                    label:'Cases',
                    data:[
                        200,
                        293,
                        300,
                        423,
                        323,
                        276,
                        189
                    ],
                    backgroundColor:[
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0,6)',
                        'rgba(153, 102, 255, 0.6)',
                        'rgba(255, 159, 68, 0.6)',
                        'rgba(255, 99, 132, 0.6)'
                    ]
                }
            ]
            }
        }
    }
    render(){
        return (
            <div className="chart">
                <Bar
                    data={this.state.chartData}
                    // width={100}
                    // height={100}
                    // size={10000}
                    options={{
                        title:{
                            display:true,
                            text:"Cities with Cases of CoronaVirus"
                        }  
                    }}
                />
            </div>
        )
    }
}

export default Chart;