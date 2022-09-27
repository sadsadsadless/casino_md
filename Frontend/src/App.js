import './App.css';

import React from "react"
import Header from "./Components/Header"
import MainContent from "./Components/MainContentPeople"
import MainContent2 from "./Components/MainContentBar"
import MainContent3 from "./Components/MainContentGame"
import Footer from "./Components/Footer"


class App extends React.Component {

    // Constructor
    constructor(props) {
        super(props);


        this.state = {
          seconds: 0
        };
    }

    tick() {
        this.setState(state => ({
            seconds: state.seconds + 1
        }));
    }


    componentDidMount() {
        this.interval = setInterval(() => document.location.reload(), 1000);
    }

    render() {
        return (
        <div class="box">
            <Header />
            <body>
                <MainContent />
                <MainContent2 />
            </body>
            <Footer />
        </div>
        );
  }
}

export default App;
