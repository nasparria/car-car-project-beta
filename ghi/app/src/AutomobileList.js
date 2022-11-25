import React from 'react'
import { Link } from 'react-router-dom'

class AutomobileList extends React.Component {
    constructor(props) {
        super(props)
        this.state = {autos: []}
    }

    async componentDidMount() {
        const response = await fetch('http://localhost:8100/api/automobiles/')
        if (response.ok) {
          const data = await response.json()
          this.setState({ autos: data.autos })
        }
      }  

    render () {
        return (
            <>
            <h1>Automobiles <Link to="new/"><button className="btn btn-primary btn-lg">Create an Automobile</button></Link></h1>
            <table className="table table-striped">
              <thead>
                <tr>
                  <th>VIN</th>
                  <th>Color</th>
                  <th>Year</th>
                  <th>Model</th>
                  <th>Manufacturer</th>
                </tr>
              </thead>
              <tbody>
                {this.state.autos.map(auto => {
                  return (
                    <tr key={auto.id}>
                      <td>{ auto.vin }</td>
                      <td>{ auto.color }</td>
                      <td>{ auto.year }</td>
                      <td>{ auto.model.name }</td>
                      <td>{ auto.model.manufacturer.name }</td>                 
                    </tr>
                  );
                })}
              </tbody>
            </table>
            </>
        )        
    }
}

export default AutomobileList