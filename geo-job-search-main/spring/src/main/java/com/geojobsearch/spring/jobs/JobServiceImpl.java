package com.geojobsearch.spring.jobs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.geojobsearch.spring.jobs.dao.JobDao;
import com.geojobsearch.spring.jobs.models.Job;

@Service
public class JobServiceImpl implements JobService {
    @Autowired
    private JobDao jobDao;

    @Override
    public String addJob(Job newJob) {
        try {
            jobDao.save(newJob);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Saved";
    }

    @Override
    public Job getJob(Integer id) {
        return jobDao.findById(id).get();
    }

    @Override
    public String updateJob(Job updatedJob) {
        try {
            jobDao.save(updatedJob);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Updated";
    }

    @Override
    public String deleteJob(Integer id) {
        try {
            jobDao.deleteById(id);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Deleted";
    }

    @Override
    public Iterable<Job> allJobs() {
        return jobDao.findAll();
    }

    @Override
    public Integer count() {
        return jobDao.getCount();
    }
}