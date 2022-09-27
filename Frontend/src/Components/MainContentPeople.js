import React from "react"
import API from "./API"
let api = new API()

function prettyPeople(data){
    console.log(data);
    let listItems = Object.keys(data).map((name) => {
        return(
            <li>
                <div  className="App-Column-Word">
                    <div>{name}</div>
                    <div>Фишек: {data[name].chips}</div>
                    <div>Денег: {data[name].money}</div>
                    <div>Алкоголь: {data[name].drunkness}</div>
                </div>
            </li>
        );
    })

    console.log(listItems);
    return listItems;
}

class PeopleList extends React.Component {

    // Constructor
    constructor(props) {
        super(props);

        this.state = {
            items: {},
            dataLength: -1,
        }

    }

    // ComponentDidMount is used to
    // execute the code
    componentDidMount() {
        //  console.log(API.get_bar_url)
        fetch(`http://${api.get_people_url}/get_people_list`)
        .then((res) => res.json())
        .then((json) => {

            for (let name of json.list) {

                fetch(
                `http://${api.get_people_url}/get_person_info?name=${name}`
                )
                .then((res) => res.json())
                .then((json) => {
                    let dct = this.state.items;
                    dct[name] = json;
                    this.setState({items: dct});
//                    console.log(Object.keys(this.items).length);
//                    console.log(this.items);
                });
            }


            this.setState({dataLength: json['list'].length});

        })
    }

    render() {
        let { items, dataLength } = this.state;

        if (Object.keys(items).length != dataLength) {
            return <div><h1> Please wait some time.... </h1></div>
        }

        return (
            <main className="MainContentPeople">
              <div className="App-table-people">
                <div className="wrap-People">
                  <div className="App-table"> <h3>Список и кол-во людей:
                    {Object.keys(items).length}</h3>
                      <div className="App-table-Info">
                        {prettyPeople(items)}
                      </div>
                  </div>
                </div>
              </div>
            </main>
        );
    }
}

export default PeopleList;