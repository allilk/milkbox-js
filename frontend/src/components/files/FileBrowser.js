import React, { Component, Fragment } from "react";
import { connect, Provider } from 'react-redux';
import PropTypes from 'prop-types';
import { GetFiles } from '../../actions/files';

export class FileBrowser extends Component {
    static propTypes = {
        files: PropTypes.array.isRequired
    }
    componentDidMount() {
        console.log('mounted!');
        this.props.GetFiles();
    }
    render(){
        return (
            <Fragment>
                { this.props.files.map((item, index) => (
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
                ))}
            </Fragment>
        )
    }
}

const mapStateToProps = (state) => ({
    files: state.files.files
});
export default connect(mapStateToProps, {GetFiles})(FileBrowser);
