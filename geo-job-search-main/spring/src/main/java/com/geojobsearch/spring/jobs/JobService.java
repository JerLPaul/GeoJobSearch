package com.geojobsearch.spring.jobs;

import com.geojobsearch.spring.jobs.models.Job;


public interface JobService {
    public String addJob(Job newJob);

    public Job getJob(Integer id);
    
    public String updateJob(Job updatedJob);

    public String deleteJob(Integer id);

    public Iterable<Job> allJobs();

    public Integer count();
}
