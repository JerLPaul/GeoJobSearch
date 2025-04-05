package com.geojobsearch.spring.jobs.dao;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import com.geojobsearch.spring.jobs.models.Job;

public interface JobDao extends CrudRepository<Job, Integer> {

    @Query("SELECT COUNT(*) FROM Job")
    Integer getCount();
}
