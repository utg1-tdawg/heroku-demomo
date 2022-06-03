import { useState, useEffect } from "react";

function App() {
  const [envData, setEnvData] = useState(null);
  const [dbData, setDbData] = useState(null);

  useEffect(() => {
    fetch("https://heroku-demomo.herokuapp.com/api")
      .then((res) => res.json())
      .then((data) => {
        setEnvData(data["env"]);
        setDbData(data["db"]);
      });
  }, []);

  return (
    <div>
      <h1>Hello world</h1>
      <div>{`Environment variable: ${envData}`}</div>
      <div>{`DB: ${dbData}`}</div>
    </div>
  );
}

export default App;
