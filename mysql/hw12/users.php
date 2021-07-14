<?php

$qb1 = Flight::get('em')->createQueryBuilder();
$qb1->select('role.user_id')
    ->from('App\Entities\Role', 'role')
    ->where($qb1->expr()->eq('role.hub_id', $hub->id));

$qb2 = Flight::get('em')->createQueryBuilder();
$qb2->select(['user.id'])
    ->from('App\Entities\User', 'user')
    ->where($qb2->expr()->in('user.id', $qb1->getDQL()))
    ->orderBy('user.user_name', 'ASC')
    ->setFirstResult($offset)
    ->setMaxResults(APP_QUERY_LIMIT);

$users_ids = $qb2->getQuery()->getResult();
$users = array_map(fn($n) => Flight::get('em')->find('App\Entities\User', $n['id']), $users_ids);
