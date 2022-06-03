import { useState, useEffect } from "react";

function App() {
  const [apiData, setApiData] = useState(null);

  useEffect(() => {
    fetch("https://heroku-demomo.herokuapp.com/api")
      .then((res) => res.json())
      .then((data) => setApiData(data["api"]));
  }, []);

  return (
    <div>
      <h1>Hello world</h1>
      <div>{`Data fetched from api: ${apiData}`}</div>
    </div>
  );
}

export default App;
