import React, { Component } from 'react'

export default class fileBrowser extends Component {
    render() {
        var ListOfFiles = [];
        for (var i = 0; i < 10; i++) {
            ListOfFiles += i;
        } 
        return(
        <div>
            {ListOfFiles.map((item, i) => (
                <li key={i}>{item}</li>
            ))}
        </div>
            );
    }
}
