import React from "react"

function PeopleList3() {
  return (//Класс с именами людей +++
    <main className="MainContentGame">
      <div className="App-table-all">
        <div className="App-table"> Список и кол-во людей:
          <b>{getPeopleData().amount}</b>
            <div>
              {listItems}
            </div>
        </div>

        <div className="App-table">Кол-во ФИШЕК
          <li className="App-Column-Word">{getPersonInfo("John").chips}</li>
          <li className="App-Column-Word">{getPersonInfo("Victor").chips}</li>
          <li className="App-Column-Word">{getPersonInfo("Ann").chips}</li>
        </div>

        <div className="App-table">Кол-во Денег
          <li className="App-Column-Word">{getPersonInfo("John").money}</li>
          <li className="App-Column-Word">{getPersonInfo("Victor").money}</li>
          <li className="App-Column-Word">{getPersonInfo("Ann").money}</li>
        </div>
      </div>
    </main>
    );
  }
  
  //Обёртка для имен людей 
  const listItems = getPeopleList().map((name) =>
  <li className="App-Column-Word">{name}</li>
  );
   
  // инфа о конкретном человеке по его имени
  function getPersonInfo(UserName) {
    switch (UserName) {
      case "John":
        return {"chips": 100, "money": 200};
      case "Victor":
        return {"chips": 0, "money": 0};
      case "Ann":
        return {"chips": 1000, "money": 0};
      default:
        return "error";
    }
  }

   
 
 // список всех людей
  function getPeopleList() {
    return ["John", " Victor", " Ann"];
  }

  // общая инфа о людях
  function getPeopleData() {
    return {"amount": 50};
  }

//     // <Router>
//     //     <div>
//     //       <Routes>
//     //         <Route path="/Time" element={<PeopleList />}/>
//     //         {/* <Route path="/Time/1" element={<PeopleList3 />}/> */}
//     //        </Routes>
//     //     </div>
//     // </Router>,
//     // document.getElementById("server")

export default PeopleList3;