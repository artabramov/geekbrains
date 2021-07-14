<?php

$qb1 = Flight::get('em')->createQueryBuilder();
if(!empty($user_id)) {
    $qb1->select('role.id')->from('App\Entities\Role', 'role')
        ->where($qb1->expr()->eq('role.user_id', $user_id))
        ->orderBy('role.id', 'DESC')
        ->setFirstResult($offset)
        ->setMaxResults(APP_QUERY_LIMIT);

} elseif(!empty($hub_id)) {
    $qb1->select('role.id')->from('App\Entities\Role', 'role')
        ->where($qb1->expr()->eq('role.hub_id', $hub_id))
        ->orderBy('role.id', 'DESC')
        ->setFirstResult($offset)
        ->setMaxResults(APP_QUERY_LIMIT);
}

$roles_ids = $qb1->getQuery()->getResult();
$roles = array_map(fn($n) => Flight::get('em')->find('App\Entities\Role', $n['id']), $roles_ids);
