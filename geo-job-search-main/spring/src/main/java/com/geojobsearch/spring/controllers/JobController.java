package com.geojobsearch.spring.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.geojobsearch.spring.jobs.JobService;
import com.geojobsearch.spring.jobs.models.Job;

@CrossOrigin(origins = "http://localhost:3000") // replace with your React app's domain
@RestController
@RequestMapping(path = "/api/Jobs")
public class JobController {
    private JobService jobService;

    @Autowired
    JobController(JobService jobService) {
        this.jobService = jobService;
    }

    @PostMapping("/add")
    private @ResponseBody String addJob(@RequestBody Job newJob) {
        return jobService.addJob(newJob);
    }

    @GetMapping("/get/{id}")
    private @ResponseBody Job getJob(@PathVariable Integer id) {
        return jobService.getJob(id);
    }

    @PutMapping("/update")
    private @ResponseBody String updateJob(@RequestBody Job updatedJob) {
        return jobService.updateJob(updatedJob);
    }

    @DeleteMapping("/delete/{id}")
    private @ResponseBody String deleteJob(@PathVariable Integer id) {
        return jobService.deleteJob(id);
    }

    @GetMapping("/all")
    
    private @ResponseBody Iterable<Job> allJobs() {
        System.out.println(jobService.allJobs().toString());
        return jobService.allJobs();
    }

    @GetMapping("/count")
    private @ResponseBody Integer count() {
        return jobService.count();
    }
}
