import React, { Component } from 'react'
import Task from './Task'


class List extends Component {

    render() {
        return (
            <div>
                <h1>Yo I'm a list</h1>
                <Task />
            </div>
        );
    }
}

export default List;
