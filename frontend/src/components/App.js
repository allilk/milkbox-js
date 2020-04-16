import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import { HashRouter as Router, Route, Switch, Redirect } from "react-router-dom";
import { Provider } from 'react-redux';
import store from '../store';

import FileBrowser from './files/FileBrowser';

class App extends Component {
    render() {
      return (
        <Provider store={store}>
          <Router>
            <Fragment>
              <Route exact path="/files/" component={FileBrowser} />
            </Fragment>
          </Router>
        </Provider>
      )
    }
  }

ReactDOM.render(<App />, document.getElementById('app'));