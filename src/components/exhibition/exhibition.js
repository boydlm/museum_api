import React, { Component } from 'react'
import axios from '../../axios';

export default class exhibition extends Component {

    constructor(props) {
        super(props);
        this.state = {
            Exhibitions: []
        };
    }
    getExhibitionData() {
        axios
            .get(`/exhibition`, {})
            .then(res => {
                const data = res.data
                console.log(data)
                const exhibition = data.map(u =>
                    <div>
                    <p>{u.id}</p>
                    <p>{u.name}</p>
                    <p>{u.email}</p>
                    <p>{u.website}</p>
                    <p>{u.company.name}</p>
                    </div>
                    )
                this.setState({
                    exhibition
                })


            })
            .catch((error) => {
                console.log(error)
            })

    }
    componentDidMount() {
        this.getExhibitionData()
    }
    render() {

        return (
            <div></div>
        )
    }
}