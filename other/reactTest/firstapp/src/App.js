import ClassComponent from "./Components/ClassComponent";
import { Counter } from "./Components/Counter";
import { FunctionComponent } from "./Components/FunctionComponent";
import { Person } from "./Components/Person";

function App() {
  return (
    <div>
      <ClassComponent />
      <FunctionComponent />
      <Person name={"Richard"} surName={"Chalk"} age={"52"} />
      <Person name={"Linda"} surName={"Chalk"} age={"47"} />
      <Counter/>
    </div>
    
  );
};

export default App;
