import logo from './logo.svg';
import './App.css';
import NameTag from './components/NameTag';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          This is my site.
        </p>
        <a
          className="App-link"
          href="https://www.linkedin.com/in/christina--dai/"
          target="_blank"
          rel="noopener noreferrer"
        >
          This is my LinkedIn
        </a>
        <NameTag name = {"Christina"}/>
        <NameTag name = {"Dai"}/>
      </header>
    </div>
  );
}

export default App;
