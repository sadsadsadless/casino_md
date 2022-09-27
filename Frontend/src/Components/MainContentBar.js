import React from "react"
import API from "./API"
let api = new API()

function prettyBar(data){
    let listItems = Object.keys(data).map((name) => {
        return(
            <li>
                <div  className="App-Column-Word">
                    <div>{name}</div>
                    <div>Цена: {data[name].price}</div>
                    <div>Крепость: {data[name].proof}</div>
                </div>
            </li>
        );
    }
)
return listItems;
}

class Bar extends React.Component {

    // Constructor 
    constructor(props) {
        super(props);

        this.state = {
            items: {},
            DataisLoaded: false
        };
    }

    // ComponentDidMount is used to
    // execute the code 
    componentDidMount() {
    //  console.log(API.get_bar_url) 
     fetch(`http://${api.get_bar_url}/get_price_list`)
            .then((res) => res.json())
            .then((json) => {
                this.setState({
                    items: json,
                    DataisLoaded: true
                });
            })
    }
    
    render() {
        const { DataisLoaded, items } = this.state;
        if (!DataisLoaded) {return <div>
            <h1> Pleses wait some time.... </h1> </div> ;}

        return (//Класс с именами людей +++
        <main className="MainContentPeople">
          <div className="App-table-bar">
            <div className="wrap-BarStatics">
              <div className="App-table"> <h3>Информация от бара:
                {Object.keys(items).length}  Видов алкоголя</h3>
                  <div className="App-table-Info">
                    {prettyBar(items)}
                  </div>
              </div>
            </div>
          </div>
        </main>
        );
  }
}

export default Bar;