<?php

$qb1 = Flight::get('em')->createQueryBuilder();
$qb1->select('role.hub_id')
    ->from('App\Entities\Role', 'role')
    ->where($qb1->expr()->eq('role.user_id', $auth->id));

$qb2 = Flight::get('em')->createQueryBuilder();
$qb2->select(['hub.id'])
    ->from('App\Entities\Hub', 'hub')
    ->where($qb2->expr()->in('hub.id', $qb1->getDQL()))
    ->orderBy('hub.hub_name', 'ASC')
    ->setFirstResult($offset)
    ->setMaxResults(APP_QUERY_LIMIT);

$hubs_ids = $qb2->getQuery()->getResult();
$hubs = array_map(fn($n) => Flight::get('em')->find('App\Entities\Hub', $n['id']), $hubs_ids);
