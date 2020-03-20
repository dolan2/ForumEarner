import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatInputModule} from '@angular/material/input';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatTableModule} from '@angular/material/table';
import {MatSortModule} from '@angular/material/sort';
import {RawDataTableComponent} from './charts/raw-data-table/raw-data-table.component';
import {BarComponent} from './charts/bar/bar.component';
import {MatOptionModule} from '@angular/material/core';
import {MatSelectModule} from '@angular/material/select';
import {NgxChartsModule} from '@swimlane/ngx-charts';
import {LinearComponent} from './charts/linear/linear.component';
import {MenuComponent} from './menu/menu.component';
import {MatGridListModule} from '@angular/material/grid-list';
import {PieComponent} from './charts/pie/pie.component';
import {MatCardModule} from '@angular/material/card';

@NgModule({
  declarations: [
    AppComponent,
    RawDataTableComponent,
    BarComponent,
    LinearComponent,
    MenuComponent,
    PieComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatPaginatorModule,
    MatTableModule,
    MatSortModule,
    MatOptionModule,
    MatSelectModule,
    NgxChartsModule,
    MatGridListModule,
    MatCardModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
