import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Saved from './components/Saved';
import Cart from './components/Cart';
import Login from './components/Login';
import Registration from './components/Registration';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/saved" component={Saved} />
          <Route path="/cart" component={Cart} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Registration} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
