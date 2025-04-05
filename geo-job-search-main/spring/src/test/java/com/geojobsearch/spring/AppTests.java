package com.geojobsearch.spring;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.TestPropertySource;
import org.springframework.test.context.jdbc.Sql;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

import com.geojobsearch.spring.jobs.JobServiceImpl;
import com.geojobsearch.spring.jobs.dao.JobDao;
import com.geojobsearch.spring.jobs.models.Job;
import org.springframework.test.web.servlet.MockMvc; // Import the necessary class

@SpringBootTest
@TestPropertySource(locations = "classpath:test.properties")
class AppTests {

    @Autowired
    private JobServiceImpl jobsService;

    @MockBean
    private JobDao jobsDao;

    @Test
    public void testAddJob() {
        Job job = new Job(1, "Test Title", "Test Text", "Test Location", "Test Company", "Test Summary", "Test Link", "Test Salary"); // Fix: Include the missing parameter in the Job constructor
        when(jobsDao.save(any(Job.class))).thenReturn(job);

        String result = jobsService.addJob(job);
        assertEquals("Saved", result);
    }

    @Test
    public void testGetAllJobs() {
        List<Job> jobsList = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            Job job = new Job(i, "Test Title", "Test Text", "Test Location", "Test Company", "Test Summary", "Test Link", "Test Salary"); // Fix: Include the missing parameter in the Job constructor
            jobsList.add(job);
        }
        
        when(jobsDao.findAll()).thenReturn(jobsList);

        Iterable<Job> jobsIterable = jobsService.allJobs();
        List<Job> jobs = StreamSupport.stream(jobsIterable.spliterator(), false).collect(Collectors.toList());
        assertEquals(5, jobs.size());
    }

    @Test
    public void testGetJob() {
        Job job = new Job(1, "Test Title", "Test Text", "Test Location", "Test Company", "Test Summary", "Test Link", "Test Salary"); // Fix: Include the missing parameter in the Job constructor
        when(jobsDao.findById(1)).thenReturn(java.util.Optional.of(job));

        Job result = jobsService.getJob(1);
        assertEquals(job, result);
    }

    @Test
    public void testUpdatejob() {
        Job job = new Job(1, "Test Title", "Test Text", "Test Location", "Test Company", "Test Summary", "Test Link", "Test Salary"); // Fix: Include the missing parameter in the Job constructor
        when(jobsDao.save(any(Job.class))).thenReturn(job);

        String result = jobsService.updateJob(job);
        assertEquals("Updated", result);
    }

    @Test
    public void testDeleteJob() {
        Job job = new Job(1, "Test Title", "Test Text", "Test Location", "Test Company", "Test Summary", "Test Link", "Test Salary"); // Fix: Include the missing parameter in the Job constructor
        when(jobsDao.findById(1)).thenReturn(java.util.Optional.of(job));

        String result = jobsService.deleteJob(1);
        assertEquals("Deleted", result);
    }

}
