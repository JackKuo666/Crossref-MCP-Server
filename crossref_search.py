from habanero import Crossref
from typing import Dict, List, Optional, Union

class CrossrefSearch:
    def __init__(self, mailto: str = None):
        """
        Initialize Crossref search class
        :param mailto: Your email address (recommended for better API access priority)
        """
        self.cr = Crossref(mailto=mailto)

    def search_works(self, query: str, limit: int = 20, **kwargs) -> Dict:
        """
        Search for scholarly works
        """
        return self.cr.works(query=query, limit=limit, **kwargs)

    def get_work_by_doi(self, doi: str) -> Dict:
        """
        Get work information by DOI
        """
        return self.cr.works(ids=doi)

    def search_members(self, query: str = None, limit: int = 20) -> Dict:
        """
        Search for publishers/institutional members
        """
        return self.cr.members(query=query, limit=limit)

    def get_member_by_id(self, member_id: Union[str, int]) -> Dict:
        """
        Get member information by ID
        """
        return self.cr.members(ids=member_id)

    def search_funders(self, query: str = None, limit: int = 20) -> Dict:
        """
        Search for funders
        """
        return self.cr.funders(query=query, limit=limit)

    def get_funder_by_id(self, funder_id: str) -> Dict:
        """
        Get funder information by ID
        """
        return self.cr.funders(ids=funder_id)

    def search_types(self) -> Dict:
        """
        Get all available work types
        """
        return self.cr.types()

    def get_type_by_id(self, type_id: str) -> Dict:
        """
        Get work type information by ID
        """
        return self.cr.types(ids=type_id)

    def search_licenses(self) -> Dict:
        """
        Get all available license information
        """
        return self.cr.licenses()

    def get_agency_by_doi(self, doi: str) -> Dict:
        """
        Get registration agency information by DOI
        """
        return self.cr.agency(ids=doi)

    def get_journals(self, query: str = None, limit: int = 20) -> Dict:
        """
        Search for journals
        """
        return self.cr.journals(query=query, limit=limit)

if __name__ == "__main__":
    # 使用示例
    crossref = CrossrefSearch(mailto="your.email@example.com")
    
    # 搜索包含"machine learning"的文章
    results = crossref.search_works("machine learning", limit=5)
    print(results)
    
    # 通过DOI获取特定文章
    doi_result = crossref.get_work_by_doi("10.1038/nature14539")
    print(doi_result)
