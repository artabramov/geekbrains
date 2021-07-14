<?php

$qb1 = Flight::get('em')->createQueryBuilder();
if(!empty($post_status)) {

    $qb1->select('post.id')->from('App\Entities\Post', 'post')
        ->where($qb1->expr()->eq('post.hub_id', Flight::get('em')->getConnection()->quote($hub_id, ParameterType::INTEGER)))
        ->andWhere($qb1->expr()->eq('post.post_status', Flight::get('em')->getConnection()->quote($post_status, ParameterType::STRING)))
        ->orderBy('post.id', 'DESC')
        ->setFirstResult($offset)
        ->setMaxResults(APP_QUERY_LIMIT);

} elseif(!empty($post_title)) {

    $qb1->select('post.id')->from('App\Entities\Post', 'post')
        ->where($qb1->expr()->eq('post.hub_id', Flight::get('em')->getConnection()->quote($hub_id, ParameterType::INTEGER)))
        ->andWhere($qb1->expr()->like('post.post_title', Flight::get('em')->getConnection()->quote('%' . $post_title . '%', ParameterType::STRING)))
        ->orderBy('post.id', 'DESC')
        ->setFirstResult($offset)
        ->setMaxResults(APP_QUERY_LIMIT);

} elseif(!empty($post_tag)) {

    $qb2 = Flight::get('em')->createQueryBuilder();
    $qb2->select('tag.post_id')
        ->from('App\Entities\Tag', 'tag')
        ->where($qb2->expr()->eq('tag.tag_value', Flight::get('em')->getConnection()->quote($post_tag, ParameterType::STRING)));

    $qb1->select('post.id')->from('App\Entities\Post', 'post')
        ->where($qb1->expr()->eq('post.hub_id', Flight::get('em')->getConnection()->quote($hub_id, ParameterType::INTEGER)))
        ->andWhere($qb1->expr()->in('post.id', $qb2->getDQL()))
        ->orderBy('post.id', 'DESC')
        ->setFirstResult($offset)
        ->setMaxResults(APP_QUERY_LIMIT);
}

$tmp = $qb1->getQuery()->getDQL();
$posts_ids = $qb1->getQuery()->getResult();
$posts = array_map(fn($n) => Flight::get('em')->find('App\Entities\Post', $n['id']), $posts_ids);
