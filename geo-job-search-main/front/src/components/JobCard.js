import './JobCard.css';
import React from 'react';
import { Card, Button } from 'react-bootstrap';


const JobCard = ({ job }) => {
    const [expanded, setExpanded] = React.useState(false);

    const handleCardClick = () => {
        setExpanded(!expanded);
    };

    return (
        <Card onClick={handleCardClick}>
            <Card.Body>
                <Card.Title>{job.title}</Card.Title>
                <Card.Text>{job.company}</Card.Text>
                
                {expanded && (
                    <>
                        <Card.Text>{job.location}</Card.Text>
                        <Card.Text>{job.salary}</Card.Text>
                        <Card.Text>{job.summary}</Card.Text>
                        <Card.Text>{job.description}</Card.Text>
                        <Card.Link href={job.link} target="_blank">Link</Card.Link>
                    </>
                )}

            </Card.Body>
        </Card>
    );
}

export default JobCard;