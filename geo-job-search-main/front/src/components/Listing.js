import {React, useState, useEffect } from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import './Listing.css';
import JobCard from './JobCard';

function Listing() {
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('/api/Jobs/all')
        .then(response => response.json())
        .then(data => setJobs(data))
        .catch(error => console.error('Error:', error));
    }, []);

    return (
        <Container className="container">
            <Row>
                <Col>
                    {
                        jobs.map((job, index) => (
                            <JobCard job={job}/>
                        ))
                    }
                </Col>
            </Row>
        </Container>
    );
}

export default Listing;