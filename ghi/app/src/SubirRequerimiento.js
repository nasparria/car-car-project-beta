import React from 'react'

class SubirRequerimientoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            empresa: '',
            titulo: '',
            descripcion: '',
            enlace: '',
            date: '',
            time: '',
            tipo: '',
            tipos: [],
        }
        this.handleEmpresaChange = this.handleEmpresaChange.bind(this)
        this.handleTituloNameChange = this.handleTituloNameChange.bind(this)
        this.handleEnlaceChange = this.handleEnlaceChange.bind(this)
        this.handleDateChange = this.handleDateChange.bind(this)
        this.handleTimeChange = this.handleTimeChange.bind(this)
        this.handleTipoChange = this.handleTipoChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }


    async componentDidMount() {
        //const statesHost = `${process.env.REACT_APP_ACCOUNT_API}`
        const statesHost = 'http://localhost:8080'
        const URL = statesHost + '/tipos/';
        const response = await fetch(URL);
        if (response.ok) {
            const data = await response.json();
            this.setState({ tipos: data.tipos });
        }
    }

    async handleSubmit(event) {
        event.preventDefault();
        const data = { ...this.state };
        delete data.tipos;

        const requerimientosHost = 'http://localhost:8080'
        const url = requerimientosHost + `/requerimientos/`;
        const fetchConfig = {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include'
        };
        const response = await fetch(url, fetchConfig);
        if (response.ok) {
            let successTag = document.getElementById('success-message');
            let formTag = document.getElementById('create-owner-form');
            successTag.classList.remove('d-none');
            formTag.classList.add('d-none');
            this.setState({
                empresa: '',
                titulo: '',
                descripcion: '',
                enlace: '',
                date: '',
                time: '',
                tipo: '',
            });
        }
    }

    handleEmpresaChange(event) {
        const value = event.target.value;
        this.setState({ empresa: value })
    }

    handleDateChange(event) {
        const value = event.target.value;
        this.setState({ date: value })
    }

    handleTituloNameChange(event) {
        const value = event.target.value;
        this.setState({ titulo: value })
    }

    handleTimeChange(event) {
        const value = event.target.value;
        this.setState({ time: value })
    }

    handleEnlaceChange(event) {
        const value = event.target.value;
        this.setState({ enlace: value })
    }

    handleTipoChange(event) {
        const value = event.target.value;
        this.setState({ tipo: value })
    }

    // async componentDidMount() {
    //     const url = 'http://localhost:8080/technicians/';

    //     const response = await fetch(url);

    //     if (response.ok) {
    //         const data = await response.json();

    //         this.setState({ technicians: data.technicians });

    //     }
    // }

    render() {
        return (
            <div className="row">
                <div className="offset-3 col-6">
                    <div className="shadow p-4 mt-4">
                        <h1>Crear un nuevo requerimiento!</h1>
                        <form onSubmit={this.handleSubmit} id="create-service-form">
                            <div className="form-floating mb-3">
                                <input onChange={this.handleEmpresaChange} value={this.state.empresa} placeholder="Empresa" required type="text" name="empresa" id="empresa" className="form-control" />
                                <label htmlFor="empresa">Empresa</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleTituloNameChange} value={this.state.titulo} placeholder="Titulo" required type="text" name="titulo" id="titulo" className="form-control" />
                                <label htmlFor="titulo">Titulo</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleDateChange} value={this.state.date} placeholder="Date" required type="date" name="date" id="date" className="form-control" />
                                <label htmlFor="date">Date</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleTimeChange} value={this.state.time} placeholder="Time" required type="time" name="time" id="time" className="form-control" />
                                <label htmlFor="time">Time</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleEnlaceChange} value={this.state.enlace} placeholder="Enlace" required type="text" name="enlace" id="enlace" className="form-control" />
                                <label htmlFor="enlace">Enlace</label>
                            </div>
                            <div className="mb-3">
                                        <select onChange={this.handleTipoChange} value={this.state.tipo} required name="tipo" id="tipo" className="form-select">
                                            <option value="">Choose Your Tipo</option>
                                            {this.state.tipos.map((tipo) => {
                                                return (
                                                    <option key={tipo.id} value={tipo.abbreviation}>
                                                        {tipo.name}
                                                    </option>
                                                )
                                            })}
                                        </select>
                                    </div>
                            <button className="btn btn-primary">Crear un requerimiento!</button>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default SubirRequerimientoForm;