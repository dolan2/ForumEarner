import {Component, Input, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {Post} from '../../models/post.interface';
import {MatTableDataSource} from '@angular/material/table';
import {MatSort} from '@angular/material/sort';
import {MatPaginator} from '@angular/material/paginator';

@Component({
  selector: 'app-raw-data-table',
  templateUrl: './raw-data-table.component.html',
  styleUrls: ['./raw-data-table.component.css']
})
export class RawDataTableComponent implements OnInit, OnDestroy {

  @Input() posts: Post[];
  displayedColumns: string[] = ['position', 'date', 'age', 'stack', 'exp', 'salary', 'currency', 'taxes', 'contract_type', 'location'];
  dataSource = new MatTableDataSource(this.posts);
  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void {
    this.dataSource = new MatTableDataSource(this.posts);
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
    this.sort.disableClear = true;
  }

  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  ngOnDestroy(): void {
  }

}
