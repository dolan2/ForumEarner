import {Component, Input} from '@angular/core';
import {Bar} from '../../models/bar.class';
import {environment} from "../../../environments/environment";

@Component({
  selector: 'app-bar',
  templateUrl: './bar.component.html',
  styleUrls: ['./bar.component.css']
})
export class BarComponent {

  @Input() data: Bar[];
  @Input() yAxisLabel: string;
  view: any[] = [1100, 700];
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = false;
  showXAxisLabel = true;
  showYAxisLabel = true;
  trimYAxisTicks = false;
  xAxisLabel = 'Employees';
  colorScheme = environment.colorScheme;

}
