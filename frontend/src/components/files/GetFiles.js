import React, { Component, useState, useEffect } from 'react'
import Cookies from 'js-cookie'

const GetFiles = (folderId) => {
    const [data, setData] = useState()
    async function getFiles() {
      const response = await fetch('http://127.0.0.1:8000/api/files/?parents='+folderId, {
        method: 'get',
        credentials: 'same-origin',
        headers: {
          'X-CSRFToken': Cookies.get('crsftoken'),
          'Content-Type': 'application/json',
          'Authorization':'Token cab55363c45a54a5e5aa03f0801500f4c1e9cfde67bd749c5e592e905f1a4668'
        }
      })
      const jsonData = await response.json()
      console.log(jsonData)
  
      setData(jsonData)
    }
    useEffect(() => getFiles(), []);
    const displayData = data
      ? data.map((item, index) => {
          return (      
            <div key={index} className="contextM flex -mx-2">
              <div className="w-1/2 list-item marquee">
                  {item.name}
              </div>
              <div className="w-1/4 date_col">
                  {item.modified_date}
              </div>
              <div className="w-1/6">
                  {item.file_size}
              </div>
            </div>
          )

        })
      : 'loading content!'
  
    return <div>{displayData}</div>
  }
  
  export default GetFiles