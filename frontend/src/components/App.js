import React, { Component } from 'react'
import ReactDOM from 'react-dom'

import GetFiles from './files/GetFiles'

const App = () => {
    const folderID = '17ZQacYVhoVuOTlf4sQ3aquX2CV5X5QcV';
    return <div className="grid grid-cols-1 gap-1">
         {GetFiles(folderID)}
    </div>
  }

ReactDOM.render(<App />, document.getElementById('app'))