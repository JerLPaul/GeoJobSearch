package com.geojobsearch.spring.jobs.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity // This tells Hibernate to make a table out of this class
@Table(name = "jobs")
public class Job {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "title", nullable = false)
    private String title;

    @Column(name = "description")
    private String description;

    @Column(name = "location")
    private String location;

    @Column(name = "company")
    private String company;

    @Column(name = "summary")
    private String summary;

    @Column(name = "link")
    private String link;

    @Column(name = "salary")
    private String salary;

    public Job() {

    }

    public Job(Integer id, String title, String description, String location, String company, String summary, String link, String salary) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.location = location;
        this.company = company;
        this.summary = summary;
        this.link = link;
        this.salary = salary;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }

    @Override
    public String toString() {
        return "Job [id=" + id + "\n title=" + title + "\n description=" + description + "\n location=" + location + "\n company=" + company + "\n summary=" + summary + "\n link=" + link + "\n salary=" + salary + "]";
    }

    
}