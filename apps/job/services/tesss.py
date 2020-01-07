# if not page:
#     page = 1
# try:
#     page = int(page)
# except:
#     return {"error": "parameter page must be integer"}, 400
# job_cat_list_ = JobCategory.query.paginate(per_page=20, page=page)
#
# if not job_cat_list_.total:
#     return {"message": "job category is empty"}, 204
#
# result = []
# for item in job_cat_list_.items:
#     result.append({"id": item.id, "name": item.name})
#
# meta = {
#     "total_data": job_cat_list_.total,
#     "total_pages": job_cat_list_.pages,
#     "total_data_per_page": job_cat_list_.per_page,
#     "next": "?page={}".format(job_cat_list_.next_num) if job_cat_list_.has_next else None,
#     "prev": "?page={}".format(job_cat_list_.prev_num) if job_cat_list_.has_prev else None
# }
# return {"data": result, "meta": meta}